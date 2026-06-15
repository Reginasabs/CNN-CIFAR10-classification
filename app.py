import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load Trained Model

model = tf.keras.models.load_model("cifar10_model.keras")

st.title("Deep Learning-based Multi-Class Image Classification")

st.write("Upload an image and let the CNN classify it.")
classes = [
    'Airplane',
    'Automobile',
    'Bird',
    'Cat',
    'Deer',
    'Dog',
    'Frog',
    'Horse',
    'Ship',
    'Truck'
]

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )
    # Resize Image

    img = image.resize((32,32))

    # Convert to NumPy Array

    img_array = np.array(img)

    # Normalize

    img_array = img_array / 255.0

    # Add Batch Dimension

    img_array = np.expand_dims(
        img_array,
        axis=0
    )
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)

    predicted_class = classes[class_index]
    st.success(
        f"Prediction: {predicted_class}"
    )
    confidence = np.max(prediction)

    st.write(
        f"Confidence: {confidence:.2%}"
    )
    