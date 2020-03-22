# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:45:10 2020

@author: Anuraag
"""

import cv2

img = cv2.imread('test.jpg')

cv2.imshow("Test Image", img)

cv2.waitKey()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray test image", gray_img)

cv2.waitKey()

cv2.destroyAllWindows()

#another method
#add 0 as a parameter after the image url in the cv2.imread() method

img = cv2.imread('test.jpg', 0)

cv2.imshow("Test Image", img)

cv2.waitKey()

cv2.destroyAllWindows()