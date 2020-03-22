# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:51:06 2020

@author: Anuraag
"""

import cv2

img = cv2.imread('test.jpg')

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Image', hsv_img)
cv2.waitKey()

cv2.destroyAllWindows()

cv2.imshow('Hue Channel', hsv_img[:, :, 0])
cv2.waitKey()

cv2.imshow('Saturation Channel', hsv_img[:, :, 1])
cv2.waitKey()

cv2.imshow('Value Channel', hsv_img[:, : ,2])
cv2.waitKey()

cv2.destroyAllWindows()