from PIL import Image
import os


def convert_filename_s3(dir):
    files = os.listdir(dir)
    for filename in files:
        print(filename)
        if filename[-3:] == 'png':
            im = Image.open(dir + filename)
            im.convert('RGB').save(dir + filename[:-3] + 'jpg', "JPEG")
        elif filename[-4:] == 'webp':
            im = Image.open(dir + filename)
            im.convert('RGB').save(dir + filename[:-4] + 'jpg', "JPEG")
        elif filename[-3:] == 'tif':
            im = Image.open(dir + filename)
            im.convert('RGB').save(dir + filename[:-3] + 'jpg', "JPEG")
        elif filename[-3:] == 'tiff':
            im = Image.open(dir + filename)
            im.convert('RGB').save(dir + filename[:-4] + 'jpg', "JPEG")
        new_filename = ''.join([letter for letter in filename if
                            (letter.isalpha() or letter.isnumeric() or letter in ['-', '_','.'])])

        os.rename(dir + filename, dir + new_filename)
        os.remove(dir + filename)


if __name__ == "__main__":
    convert_filename_s3('./convert/')

