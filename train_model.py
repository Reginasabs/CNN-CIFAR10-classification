import tensorflow as tf
from tensorflow.keras import datasets
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models

# Load Dataset
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

#print("Minimum Pixel Value:", x_train.min())
#print("Maximum Pixel Value:", x_train.max())

# Display Shapes
print("Training Images:", x_train.shape)
#print("Training Labels:", y_train.shape)

print("Testing Images:", x_test.shape)
#print("Testing Labels:", y_test.shape)

model = models.Sequential()

model.add(
    layers.Conv2D(
        32,
        (3,3),
        activation='relu',
        input_shape=(32,32,3)
    )
)
model.add(
    layers.MaxPooling2D((2,2))
)
model.add(
    layers.Conv2D(
        64,
        (3,3),
        activation='relu'
    )
)
model.add(
    layers.MaxPooling2D((2,2))
)
model.add(
    layers.Conv2D(
        64,
        (3,3),
        activation='relu'
    )
)
model.add(
    layers.Flatten()
)
model.add(
    layers.Dense(
        64,
        activation='relu'
    )
)
model.add(
    layers.Dense(
        10,
        activation='softmax'
    )
)   
model.summary()
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
history = model.fit(
    x_train,
    y_train,
    epochs=10,
    validation_data=(x_test, y_test)
)
model.save("cifar10_model.keras")

print("Model Saved Successfully!")

# Class Names

#class_names = [
#   'airplane',
#   'automobile',
#   'bird',
#   'cat',
# 'deer',
#   'dog',
#   'frog',
#   'horse',
#   'ship',
#   'truck'
#]

# Display Sample Images

#import random

#plt.figure(figsize=(10,5))

#for i in range(10):

#    index = random.randint(0,49999)

#    plt.subplot(2,5,i+1)

#    plt.imshow(x_train[index])

#    plt.title(class_names[y_train[index][0]])

#   plt.axis('off')

#plt.show()