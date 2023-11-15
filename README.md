# Image Format Converter

This script utilizes the Pillow library to convert images in various formats (png, webp, tif, tiff) to the JPEG format. Additionally, it cleans up filenames by removing characters that might cause issues.

## Usage

1. Install the Pillow library if not already installed:

    ```bash
    pip install Pillow
    ```

2. Place the images you want to convert in the specified directory (`./convert/` by default).

3. Run the script:

    ```bash
    python convert_images.py
    ```

4. The script will convert images to JPEG format and clean up filenames.

## Supported Formats

- PNG
- WebP
- TIFF

## Filename Cleanup

The script removes non-alphanumeric characters, except for ['-', '_', '.'] to ensure compatibility with various systems.

## Example

Suppose you have the following files:

- `image1.png`
- `image2.webp`
- `image3.tiff`
- `image_4.tiff`
- `image#5.png`

After running the script, the files will be converted to:

- `image1.jpg`
- `image2.jpg`
- `image3.jpg`
- `image_4.jpg`
- `image5.jpg`

## Note

Make sure to backup your images before running the script, as it modifies the files in the specified directory.
