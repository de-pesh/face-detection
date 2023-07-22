import os
import sys
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

# Function to load and preprocess the images
def preprocess_images(data_dir, image_size=(128, 128)):
    images = []
    labels = []
    for label_name in os.listdir(data_dir):
        label_dir = os.path.join(data_dir, label_name)
        if not os.path.isdir(label_dir):
            continue

        label = int(label_name)  # Assuming folder names are integers representing labels

        for image_name in os.listdir(label_dir):
            image_path = os.path.join(label_dir, image_name)
            image = cv2.imread(image_path)
            if image is None:
                continue

            # Convert image to grayscale and resize to a fixed size (for simplicity)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = cv2.resize(image, image_size)

            images.append(image)
            labels.append(label)

    # Convert the lists to NumPy arrays
                # for image in images:
                #     cv2.imshow("hehe", image)
                #     cv2.waitKey(0)
                # input()
                # cv2.destroyAllWindows()
    images = np.array(images)
    labels = np.array(labels)

    return images, labels

# Define the path to the dataset folder
def get_train_test():
    data_directory = "/Users/deepesh/Desktop/Desktop/INTERN/face detection/dataset"

    # Preprocess the images and get the features (images) and labels
    images, labels = preprocess_images(data_directory)

    print(labels)
    print("done")

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.3, random_state=42)

    # Optionally, you can normalize the pixel values to a range between 0 and 1
    X_train = X_train.astype("float32") / 255.0
    X_test = X_test.astype("float32") / 255.0
    
    print(y_test, y_train)
    print(X_test, X_train)
    return X_train, X_test, y_train, y_test
# get_train_test()