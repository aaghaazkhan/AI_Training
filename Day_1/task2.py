# Task: Convert an image to grayscale, RGB, and BGR

# importing opencv
import cv2

# loading the image
img = cv2.imread("pirate.jpg") # note that the opencv initially loads the images into BGR
print("Image Loaded Successfully")

# displaying the initial image
cv2.imshow("Initial Image", img)

# converting the image to grayscale and displaying it
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", img_grayscale)

# converting the image to RGB and displaying it
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB Image", img_RGB)


# converting the RGB image to BGR and displaying it
img_BGR = cv2.cvtColor(img_RGB, cv2.COLOR_RGB2BGR)
cv2.imshow("BGR Image", img_BGR)


cv2.waitKey(0)
cv2.destroyAllWindows()