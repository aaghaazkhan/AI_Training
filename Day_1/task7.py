# Task: Drawing shapes and text on images

# importing opencv
import cv2

# loading and displaying the original image
img = cv2.imread("pirate.jpg")
print("Image Loaded Successfully")
cv2.imshow("Original Image", img)

cv2.line(img, (0, 0), (200, 600), (0, 0, 255), 3) # image, position, color, thickness
cv2.rectangle(img, (200, 100), (300, 400), (255, 0, 0), 2) # image position, color, thickness
cv2.circle(img, (100, 100), 50, (0, 255, 0), 2) # image, centre, radius, thickness
cv2.putText(img, "PIRATE", (300, 330), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2) # image, text, position, font, scale, color, thickness

cv2.imshow("Edited Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()