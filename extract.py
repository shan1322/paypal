from PIL import Image,ImageColor
from numpy import array
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
im=Image.open('sample.jpeg').convert('L')
im.save('greyscale.png')
im1=im.load()
x,y = im.size
pixels = [[0]*y for i in range(x)]
for i in range(x):
    for j in range(y):
        pixels[i][j] = im1[i,j]
print(pixels)