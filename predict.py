import tensorflow as tf
from PIL import Image
import numpy as np

# Load model
model = tf.keras.models.load_model("cifar10_model.keras")

# CIFAR-10 classes
class_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]

# Get image filename from user
image_path = input("Enter image filename (including path if needed): ")

# Open image
img = Image.open(image_path)

# Convert to RGB
img = img.convert("RGB")

# Resize to CIFAR-10 dimensions
img = img.resize((32, 32))

# Convert to array
img_array = np.array(img)

# Normalize (same as training)
img_array = img_array / 255.0

# Add batch dimension
img_array = np.expand_dims(
    img_array,
    axis=0
)

# Predict
prediction = model.predict(img_array)

predicted_class = np.argmax(prediction)
confidence = np.max(prediction) * 100

print("\nPrediction Result")
print("------------------")
print("Predicted Class:", class_names[predicted_class])
print(f"Confidence: {confidence:.2f}%")