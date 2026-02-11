# We will be doing the data augmentation here on the train split
# I will be creating 10 augmented images per train image and also respective labels for them

# importing the libraries
import os
import cv2
import albumentations as A

# defining the image and labels path
images_path = "tattoo_dataset/images/train"
labels_path = "tattoo_dataset/labels/train"

# transformations that I am going to apply
augmentation = A.Compose([
    A.HorizontalFlip(p=0.55),
    A.VerticalFlip(p=0.55),
    A.RandomBrightnessContrast(p=0.5),
    A.Rotate(limit=15, p=0.4),
    A.Blur(blur_limit=(5,5), p=0.3)
],
# defining boundary box parameters
# we do this so that the boundary boxes are fit accordingly to the augmented new images
bbox_params=A.BboxParams(
    format="yolo",
    label_fields=["class_labels"], # class labels (0 - tattoo)
    clip=True # clip = True is used when a bounding box goes outside the image after augmentation so it brings the boundary box back inside the image.
))

## --- READ LABEL FUNCTION BEGINS ---
# Reading YOLO label file
def read_label(label_path):
    bboxes = []
    class_labels = []
    with open(label_path, "r") as f:
        for line in f:
            cls, x, y, w, h = map(float, line.split())
            bboxes.append([x, y, w, h])
            class_labels.append(int(cls))

    return bboxes, class_labels
## --- READ LABEL FUNCTION ENDS ---


for img_name in os.listdir(images_path):

    img_path = os.path.join(images_path, img_name)
    label_path = os.path.join(labels_path, img_name.rsplit(".",1)[0] + ".txt")
    image = cv2.imread(img_path)
    bboxes, class_labels = read_label(label_path)

    # 10 augmented images per train image
    for i in range(10):
        augmented = augmentation(image=image, bboxes=bboxes, class_labels=class_labels)

        new_img = augmented["image"]
        new_boxes = augmented["bboxes"]
        new_labels = augmented["class_labels"]
        new_name = img_name.rsplit(".",1)[0] + f"_augmented{i}.jpg"
        new_img_path = os.path.join(images_path, new_name)
        new_label_path = os.path.join(labels_path, new_name.replace(".jpg", ".txt"))

        # saving the augmented image
        cv2.imwrite(new_img_path, new_img)

        # saving the labels for augmented image
        
        with open(new_label_path, "w") as f:
            for box, cls in zip(new_boxes, new_labels):
                x, y, w, h = box
                f.write(f"{cls} {x} {y} {w} {h}")

print("Augmentation Completed.")