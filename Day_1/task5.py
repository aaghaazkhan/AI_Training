# Task: Blurring, erosion, dilation operations on an image

# importing the libraries
import cv2
import numpy as np

# loading the original image
img = cv2.imread("pirate.jpg")
print("Image Loaded Successfully")

# Blurring

# There are 3 types of blurring:
# 1. Averaging: Used for basic noise reduction
# 2. Gaussian: Used for general smoothing, preprocessing
# 3. Bilateral: Used for edge-preserving noise reduction

img_averaging = cv2.blur(img, (3,3))
img_gaussian = cv2.GaussianBlur(img, (3,3), 0)
img_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("Averaging", img_averaging)
cv2.imshow("Gaussian", img_gaussian)
cv2.imshow("Bilateral", img_bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()


# defining the kernal
kernel = np.ones((5,5), np.uint8)

# Erosion
# Erosion makes the white areas shrink and the small white noise disappears

img_erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow("Erosion", img_erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Dilation
# Dilation expands the white regions (objects become thicker)

img_dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Dilation", img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()