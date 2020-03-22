# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:35:35 2020

@author: Anuraag
"""

import cv2

img = cv2.imread('test.jpg')

cv2.imshow("Test Image", img)

cv2.waitKey()

cv2.destroyAllWindows()