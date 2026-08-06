# CNN Image Classifier

A deep learning image classification web application built using **TensorFlow** and **Streamlit**.

## Overview

This project uses a **Convolutional Neural Network (CNN)** trained on the **CIFAR-10 dataset** to classify uploaded images into one of ten categories. The Streamlit interface enables users to upload an image and view the predicted class along with the model's confidence score.

## Features

* Upload JPG, JPEG, or PNG images
* Automatic image preprocessing
* CNN-based image classification
* Displays predicted class and confidence score
* Simple and interactive Streamlit interface

## Technologies Used

* Python
* TensorFlow / Keras
* Streamlit
* NumPy
* Pillow (PIL)

## CIFAR-10 Classes

* Airplane
* Automobile
* Bird
* Cat
* Deer
* Dog
* Frog
* Horse
* Ship
* Truck

## How to Run

1. Clone the repository.
2. Install the required dependencies.
3. Place the trained model (`cnn5_cifar10.keras`) in the project folder.
4. Run:

   ```bash
   streamlit run app.py
   ```

## Future Improvements

* Support additional datasets
* Improve model accuracy with data augmentation
* Deploy the application to Streamlit Community Cloud
* Add Grad-CAM visualizations for model explainability

⭐ If you found this project useful, consider giving it a star!
