""" This module will be used for creating image """
from PIL import Image

from colors import randomColor


def imageCreator():
    img = Image.open("SZE3.png") # img contain image. should contain path to image
    pixels = img.load()  # create the pixel map
    for i in range(img.size[0]): # for every pixel:
        # Если добавить цвета в эту строчку то будет радужная картинка для каждой вертикальной линии
        for j in range(img.size[1]):
            if pixels[i,j] == (0,0,0): # black #000000
                pixels[i,j] = randomColor()
            if pixels[i,j] == (255, 255, 255): # white
                pixels[i, j] = randomColor()
            if pixels[i,j] == (0, 36, 255): # red #ff0000
                pixels[i, j] = randomColor()
            if pixels[i,j] == (246, 0, 255): # green
                pixels[i, j] = randomColor()
            if pixels[i,j] == (255, 234, 0): # green
                pixels[i, j] = randomColor()
    return img.show()


for i in range(0,2):
    imageCreator()