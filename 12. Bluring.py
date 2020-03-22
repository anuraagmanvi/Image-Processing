# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:39:02 2020

@author: Anuraag
"""

import cv2
import numpy as np

img = cv2.imread('test.jpg')
cv2.imshow("Original", img)
cv2.waitKey()

k_3 = np.ones((10, 10), np.float32)/100

blurred = cv2.filter2D(img, 0, k_3)
cv2.imshow("Blurred", blurred)
cv2.waitKey()
cv2.destroyAllWindows()

#Other blurring algorithms
#Averaging filter blurring

cv2.imshow("Original Box BLur", img)
cv2.waitKey()

blur_avg = cv2.blur(img, (10, 10))
cv2.imshow("Averaging Filter BLur", blur_avg)
cv2.waitKey()

#blur_gaus = cv2.GaussianBlur(img, (10, 10), 0)
#cv2.imshow("Gaussian Filter BLur", blur_gaus)
#cv2.waitKey()

blur_med = cv2.medianBlur(img, 5)
cv2.imshow("Median Filter BLur", blur_med)
cv2.waitKey()

blur_bi = cv2.bilateralFilter(img, 5, 75, 75)
cv2.imshow("Bilateral Filter BLur", blur_bi)
cv2.waitKey()

cv2.destroyAllWindows()