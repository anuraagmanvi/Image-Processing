# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:43:15 2020

@author: Anuraag
"""

import cv2
import numpy as np

img = cv2.imread('test.jpg')

#height and width of the image
height, width = img.shape[:2]

#divide by 2 to rotate the image around its center
rot_matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)

img_rot = cv2.warpAffine(img, rot_matrix, (width, height))

cv2.imshow('Rotated image', img_rot)
cv2.waitKey()
cv2.destroyAllWindows()