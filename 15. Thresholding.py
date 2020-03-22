# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:04:38 2020

@author: Anuraag
"""

import cv2
import numpy as np

img = cv2.imread('test.jpg', 0)
cv2.imshow("Original", img)
cv2.waitKey()

ret, thresh1 = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh1)
cv2.waitKey()

ret, thresh2 = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", thresh2)
cv2.waitKey()

ret, thresh3 = cv2.threshold(img, 160, 255, cv2.THRESH_TRUNC)
cv2.imshow("Threshold Truncate", thresh3)
cv2.waitKey()

ret, thresh4 = cv2.threshold(img, 160, 255, cv2.THRESH_TOZERO)
cv2.imshow("Threshold ToZero", thresh4)
cv2.waitKey()

ret, thresh5 = cv2.threshold(img, 160, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("Threshold ToZero Inverse", thresh5)
cv2.waitKey()

cv2.destroyAllWindows()