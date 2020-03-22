# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:42:44 2020

@author: Anuraag
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg')

cv2.circle(img, (350, 350), 100, (15, 75, 50), -1)
cv2.imshow("CIRCLE", img)
cv2.waitKey(0)

cv2.putText(img, "Research", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (100, 170, 0), 3)
cv2.imshow("CIRCLE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()