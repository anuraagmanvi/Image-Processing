# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:41:06 2020

@author: Anuraag
"""

import cv2
import numpy as np

img = cv2.imread('test.jpg')
cv2.imshow("Original", img)
cv2.waitKey()

dst = cv2.fastNlMeansDenoisingColored(img, None, 6, 6, 7, 21)
cv2.imshow("Denoised", dst)
cv2.waitKey()

cv2.destroyAllWindows()