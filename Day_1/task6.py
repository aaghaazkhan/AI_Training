# Task: Thresholding and edge detection 

# importing opencv
import cv2

# loading and displaying the original image
img = cv2.imread("pirate.jpg")
cv2.imshow("Original Image", img)

# we need to convert the images to grayscale before edge detection
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", img_grayscale)

# Threshold
_, threshold = cv2.threshold(img_grayscale, 127, 255, cv2.THRESH_BINARY) # converts the image into binary image
# If brightness above 127, convert it to 255 (white), else 0 (black)
cv2.imshow("Threshold", threshold)

# Edge Detection
edges = cv2.Canny(img_grayscale, 100, 200)
# 100 here is the minimum change in brightness to consider for the edge detection
# 200 is a strong change in brightness
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()