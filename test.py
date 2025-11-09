from matplotlib import pyplot
import numpy as np
from math import *
import pprint

#vsechny_x = linspace(-pi*1, pi*1, 100000)
#y = []
#
#for x in vsechny_x:
#    y.append(cos(1/x))
#    print(f"{x}")
#
#pyplot.plot(vsechny_x, y)
#pyplot.show()

img = np.zeros((1024,1024))
for x in range(img.shape[1]):
    for y in range(img.shape[0]):
        img[y,x] = x ^ y
pyplot.imshow(img, cmap=None)
pyplot.show()