# Task: Resize, Crop, Rotate, and Flip an Image

# importing opencv
import cv2

# loading the image
img = cv2.imread("pirate.jpg")
print("Image Loaded Successfully")
print(f"Image Size: ({img.shape})")

# obtaining the original height and width of the image
height = img.shape[0]
width = img.shape[1]

# displaying the initial image
cv2.imshow("Initial Image", img)

# resizing the image to half of it's original size and displaying it
new_width = width // 2
new_height = height // 2
img_resized = cv2.resize(img, (new_width, new_height)) # image, (width, height)
cv2.imshow("Resized Image", img_resized)
print(f"Resized Image Size: ({img_resized.shape})")

# cropping the image and displaying it
# For cropping the image, there's no module by opencv and hence we do it manually by slicing the image
img_cropped = img[100:400, 200:600] # img[y1:y2, x1:x2]
# this means:
# - start at pixel row 100 and end at 400
# = start at pixel column 200 and end at 600
cv2.imshow("Cropped Image", img_cropped)

# rotating the image and displaying it
img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated Image", img_rotated)
# different rotation parameters:
# - cv2.ROTATE_90_COUNTERCLOCKWISE
# - cv2.ROTATE_180

# # flipping the image and displaying it
img_flipped = cv2.flip(img, -1)
cv2.imshow("Flipped Image", img_flipped)
# -1 flips both horizontally, and vertically
# 1 flips horizontally only
# 0 flips vertically only

cv2.waitKey(0)
cv2.destroyAllWindows()