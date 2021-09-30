""" This module will contain all need and reuired colors """

import random


# use this function to create random colors on RGB format (decimal)

def randomColor():
    randCol = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return randCol

