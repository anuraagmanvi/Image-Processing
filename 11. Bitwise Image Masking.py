# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:16:22 2020

@author: Anuraag
"""

import cv2
import numpy as np

#Making a square
square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)
cv2.imshow("Square", square)
cv2.waitKey()

#Making an elipse
elipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(elipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
cv2.imshow("Elipse", elipse)
cv2.waitKey()


bitwise_and = cv2.bitwise_and(square, elipse)
cv2.imshow("AND", bitwise_and)
cv2.waitKey()

bitwise_or = cv2.bitwise_or(square, elipse)
cv2.imshow("OR", bitwise_or)
cv2.waitKey()

bitwise_xor = cv2.bitwise_xor(square, elipse)
cv2.imshow("XOR", bitwise_xor)
cv2.waitKey()

bitwise_not = cv2.bitwise_not(square, elipse)
cv2.imshow("NOT", bitwise_not)
cv2.waitKey()

cv2.destroyAllWindows()