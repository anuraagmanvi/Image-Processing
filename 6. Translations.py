# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:30:15 2020

@author: Anuraag
"""

import cv2
import numpy as np

img = cv2.imread('test.jpg')

#height and width of the image
height, width = img.shape[:2]

q_height, q_width = height/4, width/4


#T is the translation matrix
#   |1 0 Tx|
#   |0 1 Ty|

T = np.float32([[1, 0, q_width], [0, 1, q_height]])

img_trans = cv2.warpAffine(img, T, (width, height))
cv2.imshow('Translated Image', img_trans)
cv2.waitKey()
cv2.destroyAllWindows()