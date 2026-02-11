# We will be first splitting the images and labels properly into train, test, and val split

# importing the libraries
import os
import shutil
from sklearn.model_selection import train_test_split

# defining the dir path for images and labels
images_path = "tattoo_dataset/images"
labels_path = "tattoo_dataset/labels"

# storing images for splitting them
images = [image for image in os.listdir(images_path) if image.endswith((".jpg", ".png", ".webp"))]


# train, test, val split for images
train_images, temp_images = train_test_split(images, test_size=0.3, random_state=42) # 70% train, 30% temp
val_images, test_images = train_test_split(temp_images, test_size=0.33, random_state=42) # 20% val, 10% test


## --- MOVE FILE FUNCTION BEGINS ---
# Function to move the images with it's respective label into train, test, and val folder
def moveFile(files, split):

    os.makedirs(f"{images_path}/{split}", exist_ok=True)
    os.makedirs(f"{labels_path}/{split}", exist_ok=True)

    for file in files:
        label = file.rsplit('.', 1)[0] + '.txt'
        shutil.move(f"{images_path}/{file}", f"{images_path}/{split}/{file}")
        shutil.move(f"{labels_path}/{label}", f"{labels_path}/{split}/{label}")
## --- MOVE FILE FUNCTION ENDS ---


# Finally splitting the data
moveFile(train_images, "train")
moveFile(val_images, "val")
moveFile(test_images, "test")