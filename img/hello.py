from PIL import Image
import tempfile

import os

# 设置图片的大小，已经dpi
def set_image_dpi_resize(image):
    """
    Rescaling image to 300dpi while resizing
    :param image: An image
    :return: A rescaled image
    """
    length_x, width_y = image.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    image_resize = image.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='1.png')
    temp_filename = temp_file.name
    image_resize.save(temp_filename, dpi=(300, 300))
    return temp_filename


def set_image_dpi(image):
    """
    Rescaling image to 300dpi without resizing
    :param image: An image
    :return: A rescaled image
    """
    image_resize = image
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    temp_filename = temp_file.name
    image_resize.save(temp_filename, dpi=(450, 450))
    return temp_filename


# im = Image.open("./1.jpg")
# print(set_image_dpi(im))

SUFFIX = "_new"
WIDTH = 260
HEIGHT = 300
DPI = 450


# img = img.resize((260, 320), Image.ANTIALIAS)
# img.save("./3.jpg", dpi=(300, 300))


def changeImage(image, width, height, dpi):
    filename = getFileName(image, SUFFIX)
    image = image.resize((width, height), Image.ANTIALIAS)
    image.save(filename, dpi=(dpi, dpi))


def getFileName(image, suffix):
    filename, file_extension = os.path.splitext(image.filename)
    return filename + suffix + file_extension


def loopDir():
    directory = './'

    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            # do smth
            # continue
            # with Image.open(filename) as img:
            #     changeImage(img, WIDTH, HEIGHT, DPI)
            with Image.open(filename) as img:
                changeImage(img, WIDTH, HEIGHT, DPI)
        else:
            continue


# img = Image.open("./2.jpg")
# changeImage(img,WIDTH,HEIGHT,DPI)

loopDir()
