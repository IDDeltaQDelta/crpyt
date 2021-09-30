from PIL import Image

""" useful link for mixing image https://defpython.ru/prostoe_nalozhenie_izobrazhenii_v_Python """

img = Image.open("image/SZE3.png")
watermark = Image.open("image/6363.png")
secondmark = Image.open("image/123333.png").convert("RGBA")

img.paste(watermark, (500,100), watermark)
img.paste(secondmark, (700,700), secondmark)
img.paste(watermark, (700,700), watermark)
img.show("image/SZE3.png")