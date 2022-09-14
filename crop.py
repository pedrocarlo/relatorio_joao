import os
# import Image module
from PIL import Image

IMAGES_DIR = "imagens"
CROP_DIR = "cropped"


def button_func():
    def crop(filename):
        # open the image
        im = Image.open(IMAGES_DIR + f"/{filename}")

        left = 0
        top = 55
        right = im.width
        bottom = im.height - 127

        # crop the image
        croppedIm = im.crop((left, top, right, bottom))

        # show the image
        # croppedIm.show()
        croppedIm.save(CROP_DIR + f"/{filename}")
        im.close()

    images = os.listdir(IMAGES_DIR)
    for image in images:
        crop(image)
