# CIFAR-10 Image Classification using Convolutional Neural Networks (CNN)

## Project Overview

This project implements an image classification system using a Convolutional Neural Network (CNN) trained on the CIFAR-10 dataset. The model classifies images into one of ten categories and is deployed through a Streamlit web application that allows users to upload images and obtain predictions.

## Dataset

The project uses the CIFAR-10 dataset, a benchmark dataset in computer vision containing 60,000 color images of size 32 × 32 pixels distributed across 10 classes.

### Classes

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

### Dataset Distribution

- Training Images: 50,000
- Testing Images: 10,000

Dataset Source:
https://www.cs.toronto.edu/~kriz/cifar.html

---

## Objectives

- Develop a Convolutional Neural Network for image classification.
- Train and evaluate the model using the CIFAR-10 dataset.
- Deploy the trained model through a Streamlit web interface.
- Demonstrate practical application of deep learning for image recognition.

---

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Streamlit

---

## Model Architecture

The CNN architecture consists of:

1. Convolutional Layer (Conv2D)
2. Max Pooling Layer
3. Convolutional Layer (Conv2D)
4. Max Pooling Layer
5. Flatten Layer
6. Dense Hidden Layer
7. Output Layer with Softmax Activation

### Key Components

- Convolutional Neural Networks (CNN)
- ReLU Activation Function
- Max Pooling
- Softmax Classification
- Adam Optimizer

---

## Training Process

The model was trained using:

- Loss Function: Sparse Categorical Crossentropy
- Optimizer: Adam
- Evaluation Metric: Accuracy
- Dataset: CIFAR-10

---

## Results

The model successfully learned to classify images into ten categories and achieved satisfactory classification performance on the test dataset.

### Sample Predictions

The Streamlit application allows users to upload images and receive predictions such as:

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

---

## Project Structure

```text
cifar10/

├── app.py
├── train.py
├── README.md
├── cifar.keras
└── requirements.txt
```

---

## Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train the Model

```bash
python train.py
```

### Launch the Streamlit Application

```bash
streamlit run app.py
```

---

## Learning Outcomes

This project demonstrates:

- Image preprocessing
- Deep learning model development
- Convolutional Neural Networks
- Image classification
- Model deployment using Streamlit
- End-to-end machine learning workflow

---

## Future Enhancements

- Data augmentation
- Transfer learning using pre-trained models
- Hyperparameter optimization
- Deployment to cloud platforms
- Support for real-time image classification

---

## Author

Dr. Sr. Italia Joseph Maria

MCA Department

Marian College Kuttikkanam (Autonomous)

Kerala, India