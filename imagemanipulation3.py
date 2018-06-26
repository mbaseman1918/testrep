from PIL import Image, ImageDraw
from random import randint

width = 500
height = 500

img = Image.new("RGB", (width, height))

draw = ImageDraw.Draw(img)

draw.rectangle(((0, 0), (width, height)), fill = "white")
draw.rectangle(((100, 100), (300, 300)), fill = "lightblue")
color = (256, 128, 128)
draw.line((0, 0, width, height), fill = color)
draw.line((0, height, width, 0), fill = color)

circle_x = width/2
circle_y = height/2
circle_radius = 100
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill = "lightgreen")

for i in range(1000):
    x0 = randint(0, width)
    y0 = randint(0, height)
    x1 = randint(0, width)
    y1 = randint(0, height)
    line_width = randint(1, 40)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    draw.line((x0, y0, x1, y1), fill = (red, green, blue), width = line_width)

img.show()
