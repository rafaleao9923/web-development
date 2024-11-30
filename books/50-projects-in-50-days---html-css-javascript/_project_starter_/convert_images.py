import os
from PIL import Image

def convert_jpg_to_png(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as img:
                new_filename = os.path.splitext(filename)[0] + '.png'
                new_filepath = os.path.join(directory, new_filename)
                img.save(new_filepath, 'PNG')
            print(f"Converted {filename} to {new_filename}")

if __name__ == "__main__":
    image_directory = "/home/hung/Public/leao/web-development/books/50-projects-in-50-days---html-css-javascript/_project_starter_/images/"
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)
    convert_jpg_to_png(image_directory)
