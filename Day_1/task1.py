# Task: Read an image, displaying it, and then saving the image back.

# importing opencv
import cv2

# reading the image
img = cv2.imread("pirate.jpg")
print("Image Loaded Successfully")

# displaying the image
cv2.imshow("Pirate", img) # shows the image window
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # closes the image window

# saving the image
cv2.imwrite("pirate2.jpg", img)
print("Image Saved Successfully")