# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:50:41 2020

@author: Anuraag
"""

import cv2
import numpy as np

img = cv2.imread('test.jpg')

img_scaled = cv2.resize(img, None, fx=0.75, fy=0.75)
cv2.imshow('Scaled Image-Linear', img_scaled)
cv2.waitKey()

img_scaled = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaled Image-Cubic', img_scaled)
cv2.waitKey()

img_scaled = cv2.resize(img, (900, 400), interpolation=cv2.INTER_AREA)
cv2.imshow('Scaled Image-Skewed', img_scaled)
cv2.waitKey()
cv2.destroyAllWindows()