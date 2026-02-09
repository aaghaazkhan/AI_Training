# Task: Perform Image Augmentations using "almbumentations"

# importing the libraries
import albumentations as A
import cv2

# loading the image
img = cv2.imread("pirate.jpg")
print("Image Loaded Successfully")

# displaying the initial image
cv2.imshow("Original Image", img)

# transformations that we want to apply to the image:
# p -> probability of the particular transformation to be applied
transform = A.Compose([
        A.Blur(blur_limit=(3,3), p=0.5),
        A.Resize(512, 512),
        A.RandomBrightnessContrast(p=0.9),
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.5)
])

# apply augmentation
augmented = transform(image=img)

# get the augmented image
img_augmented = augmented['image']

# display the augmented image
cv2.imshow("Augmented Image", img_augmented)

# saving the augmented image
cv2.imwrite("pirate_augmented.jpg", img_augmented)
print("Image Saved Successfully")

cv2.waitKey(0)
cv2.destroyAllWindows()