from PIL import Image
import random

from randcolor import randomColor

a = randomColor()
print(a)
a = list(a)
print(a)
for i in a:
    i = i - 1

print(a)


