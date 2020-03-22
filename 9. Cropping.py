# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:11:41 2020

@author: Anuraag
"""

import cv2
import numpy as np

img = cv2.imread('test.jpg')
height, width = img.shape[:2]

#starting top left pixel cordinates
s_row, s_col = int(height * 0.05), int(width * 0.2)

#ending bottom right pixel cordinates
e_row, e_col = int(height * 0.5), int(width * 0.8)

img_crop = img[s_row:e_row, s_col:e_col]

cv2.imshow("Original Image", img)
cv2.waitKey()
cv2.imshow("Cropped Image", img_crop)
cv2.waitKey()
cv2.destroyAllWindows()