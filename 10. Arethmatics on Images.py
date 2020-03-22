# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:51:21 2020

@author: Anuraag
"""

import cv2
import numpy as np

img = cv2.imread('test.jpg')

#create a matrix of ones and multiply it by a scaler of 100
M = np.ones(img.shape, dtype="uint8") * 75

#we use this matrix to add or subtract to increase or decrease brightness
add_img = cv2.add(img, M)
cv2.imshow("Addition operation", add_img)
cv2.waitKey()

sub_img = cv2.subtract(img, M)
cv2.imshow("Subtraction operation", sub_img)
cv2.waitKey()
cv2.destroyAllWindows()