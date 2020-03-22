# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:14:06 2020

@author: Anuraag
"""

import cv2
import numpy as np

img = cv2.imread('test.jpg')
cv2.imshow("Original", img)
cv2.waitKey()

k_sharp = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]])

img_sharp = cv2.filter2D(img, -1, k_sharp)
cv2.imshow("Sharpened", img_sharp)
cv2.waitKey()

cv2.destroyAllWindows()