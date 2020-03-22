# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:32:18 2020

@author: Anuraag
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg')

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.hist(img.ravel(), 256, [0, 256])
plt.show()

color = ('b', 'g', 'r')

for i, col in enumerate(color):
    hist2 = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist2, color = col)
    plt.xlim([0, 256])
    
plt.show()