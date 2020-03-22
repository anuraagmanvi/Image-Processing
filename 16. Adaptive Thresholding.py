# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:19:06 2020

@author: Anuraag
"""

import cv2
import numpy as np

img = cv2.imread('test.jpg', 0)
cv2.imshow("Original", img)
cv2.waitKey()

thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 6)
cv2.imshow("Threshold Mean Adaptive", thresh1)
cv2.waitKey()

ret, thresh2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Threshold Otsu's", thresh2)
cv2.waitKey()

cv2.destroyAllWindows()