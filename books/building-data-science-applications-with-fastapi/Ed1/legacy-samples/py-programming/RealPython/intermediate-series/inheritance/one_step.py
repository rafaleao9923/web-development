# https://realpython.com/inheritance-composition-python/


class MyClass:
    pass


class MyError(Exception):
    pass


c = MyClass()
print(dir(c))


o = object()
print(dir(o))


raise MyError('This is a test')
