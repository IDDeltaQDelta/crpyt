""" This module will be used for creating image """
from PIL import Image

from randcolor import randomColor


def imageCreator():
    a = randomColor()
    b = randomColor()
    c = randomColor()
    d = randomColor()
    e = randomColor()
    img = Image.open("image/SZE3.png") # img contain image. should contain path to image
    pixels = img.load()  # create the pixel map
    for i in range(img.size[0]): # for every pixel:
        # Если добавить цвета в эту строчку то будет радужная картинка для каждой вертикальной линии
        for j in range(img.size[1]):
            if pixels[i,j] == (0,0,0): # black #000000
                pixels[i,j] = a
            if pixels[i,j] == (255, 255, 255): # white
                pixels[i, j] = b
            if pixels[i,j] == (0, 36, 255): # red #ff0000
                pixels[i, j] = c
            if pixels[i,j] == (246, 0, 255): # green
                pixels[i, j] = d
            if pixels[i,j] == (255, 234, 0): # green
                pixels[i, j] = e
    return img.show()


for i in range(0,2):
    imageCreator()