import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.preprocessing import LabelEncoder
from preprocess import get_train_test

# Flatten the 2D images into 1D vectors for VGG input
X_train , X_test, y_train, y_test = get_train_test()
X_train_flattened = X_train.reshape(X_train.shape[0], 128, 128, 1)
X_test_flattened = X_test.reshape(X_test.shape[0], 128, 128, 1)

# Convert the labels to one-hot encoding using LabelEncoder
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# Define the VGG model architecture
def create_vgg_model(input_shape):
    model = models.Sequential()
    model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(256, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(len(np.unique(y_train_encoded)), activation='softmax'))  # Output layer

    return model

# Create the VGG model
vgg_model = create_vgg_model(input_shape=(128, 128, 1))

# Compile the model
vgg_model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

# Train the model on the training data
vgg_model.fit(X_train_flattened, y_train_encoded, epochs=10, batch_size=32, validation_split=0.1)

# Evaluate the model on the test data
loss, accuracy = vgg_model.evaluate(X_test_flattened, y_test_encoded)
print("Test Loss:", loss)
print("Test Accuracy:", accuracy)
