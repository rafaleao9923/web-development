## Project Structure

```
project/
├── assets/
│   ├── headers/
│   │   ├── header-1.jpg
│   │   ├── header-2.jpg
│   │   ├── header-3.jpg
│   │   ├── header-4.jpg
│   │   ├── header-5.jpg
│   │   └── header-6.jpg
│   └── avatars/
│       ├── avatar-1.jpg
│       ├── avatar-2.jpg
│       ├── avatar-3.jpg
│       ├── avatar-4.jpg
│       ├── avatar-5.jpg
│       └── avatar-6.jpg
```

## Image Sizes

```
Headers: 800x400px (JPEG, 70-80% quality)
Avatars: 100x100px (JPEG, 70-80% quality)

You can use these commands to batch resize images using ImageMagick:

For headers:
mogrify -resize 800x400^ -quality 75 -path ./assets/headers/ source/*.jpg

For avatars:
mogrify -resize 100x100^ -quality 75 -path ./assets/avatars/ source/*.jpg
```