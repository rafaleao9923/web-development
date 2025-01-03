import os
from functools import wraps
from werkzeug.utils import secure_filename
from flask import request, Blueprint, render_template, jsonify, flash,redirect, url_for as flask_url_for, g, abort, current_app
from my_app import db, ALLOWED_EXTENSIONS, babel
from my_app.catalog.models import Product, Category, ProductForm, CategoryForm
from sqlalchemy.orm import join
from flask_babel import lazy_gettext as _
import geoip2.database
from geoip2.errors import AddressNotFoundError
import boto3

catalog = Blueprint('catalog', __name__)


@catalog.before_request
def before():
    if request.view_args and 'lang' in request.view_args:
        g.current_lang = request.view_args['lang']
        request.view_args.pop('lang')


@catalog.context_processor
def inject_url_for():
    return {
        'url_for': lambda endpoint, **kwargs: flask_url_for(
            endpoint, lang=g.get('current_lang', 'en'), **kwargs
        )
    }


url_for = inject_url_for()['url_for']


def template_or_json(template=None):
    """"Return a dict from your view and this will either
    pass it to a template or render json. Use like:

    @template_or_json('template.html')
    """
    def decorated(f):
        @wraps(f)
        def decorated_fn(*args, **kwargs):
            ctx = f(*args, **kwargs)
            if request.headers.get("X-Requested-With") == "XMLHttpRequest" or not template:
                return jsonify(ctx)
            else:
                return render_template(template, **ctx)
        return decorated_fn
    return decorated


def allowed_file(filename):
    return '.' in filename and \
            filename.lower().rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@catalog.errorhandler(404)
def page_not_found(e):
    current_app.logger.error(e)
    return render_template('404.html'), 404


@catalog.route('/')
@catalog.route('/<lang>/')
@catalog.route('/<lang>/home')
@template_or_json('home.html')
def home():
    products = Product.query.all()
    current_app.logger.info(
        'Home page with total of %d products' % len(products)
    )
    return {'count': len(products)}


@catalog.route('/<lang>/product/<id>')
def product(id):
    product = Product.query.filter_by(id=id).first()
    if not product:
        current_app.logger.warning('Requested product not found.')
        abort(404)
    return render_template('product.html', product=product)


@catalog.route('/<lang>/products')
@catalog.route('/<lang>/products/<int:page>')
def products(page=1):
    products = Product.query.paginate(page=page, per_page=10)
    return render_template('products.html', products=products)


@catalog.route('/<lang>/product-create', methods=['GET', 'POST'])
def create_product():
    form = ProductForm()

    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        category = Category.query.get_or_404(
            form.category.data
        )
        image = request.files and request.files['image']
        filename = ''
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            session = boto3.Session(
                aws_access_key_id=current_app.config['AWS_ACCESS_KEY'],
                aws_secret_access_key=current_app.config['AWS_SECRET_KEY']
            )
            s3 = session.resource('s3')
            bucket = s3.Bucket(current_app.config['AWS_BUCKET'])
            if bucket not in list(s3.buckets.all()):
                bucket = s3.create_bucket(
                    Bucket=current_app.config['AWS_BUCKET'],
                    CreateBucketConfiguration={
                        'LocationConstraint': 'ap-south-1'
                    },
                )
            bucket.upload_fileobj(
                image, filename,
                ExtraArgs={'ACL': 'public-read'})
        reader = geoip2.database.Reader('GeoLite2-City_20230113/GeoLite2-City.mmdb')
        try:
            match = reader.city(request.remote_addr)
        except geoip2.errors.AddressNotFoundError:
            match = None

        product = Product(
            name, price, category, filename,
            match and match.location.time_zone or 'Localhost'
        )
        db.session.add(product)
        db.session.commit()
        flash(
            _('The product %(name)s has been created', name=name),
            'success'
        )
        return redirect(url_for('catalog.product', id=product.id))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('product-create.html', form=form)


@catalog.route('/<lang>/product-search')
@catalog.route('/<lang>/product-search/<int:page>')
def product_search(page=1):
    name = request.args.get('name')
    price = request.args.get('price')
    company = request.args.get('company')
    category = request.args.get('category')
    products = Product.query
    if name:
        products = products.filter(Product.name.like('%' + name + '%'))
    if price:
        products = products.filter(Product.price == price)
    if company:
        products = products.filter(Product.company.like('%' + company + '%'))
    if category:
        products = products.select_from(join(Product, Category)).filter(
            Category.name.like('%' + category + '%')
        )
    return render_template(
        'products.html', products=products.paginate(page=page, per_page=10)
    )


@catalog.route('/<lang>/category-create', methods=['GET', 'POST'])
def create_category():
    form = CategoryForm()

    if form.validate_on_submit():
        name = form.name.data
        category = Category(name)
        db.session.add(category)
        db.session.commit()
        flash(
            _('The category %(name)s has been created', name=name),
            'success'
        )
        return redirect(
            url_for('catalog.category', id=category.id)
        )

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('category-create.html', form=form)


@catalog.route('/<lang>/category/<id>')
def category(id):
    category = Category.query.get_or_404(id)
    return render_template('category.html', category=category)


@catalog.route('/<lang>/categories')
def categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)
