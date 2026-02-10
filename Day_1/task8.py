# Task:  Create an image processing pipeline combining the previous operations 

# importing the libraries
import cv2
import albumentations as A

# Reading an Image
img = cv2.imread("pirate.jpg")

# Resizing the Image
img = cv2.resize(img, (512, 512))

# Performing Augmentation on the Image
transform = A.Compose([
    A.HorizontalFlip(p=1),
    A.RandomBrightnessContrast(p=0.5)
])

augmented = transform(image=img)
img = augmented["image"]

# Converting the Image to Grayscale
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Applying Gaussian Blur on the Image
img_blur = cv2.GaussianBlur(img_grayscale, (5,5), 0)

# Threshold
_, threshold = cv2.threshold(img_blur, 127, 255, cv2.THRESH_BINARY)

# Performing Edge detection
edges = cv2.Canny(img_blur, 100, 200)

# Writing Text on the Original Image
cv2.putText(img, "PIRATE", (20,40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)

# Displaying the output Images
cv2.imshow("Original Image", img)
cv2.imshow("Threshold", threshold)
cv2.imshow("Edges", edges)

# Save final image
cv2.imwrite("final_img.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
