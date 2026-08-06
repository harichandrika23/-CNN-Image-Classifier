import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("cnn5_cifar10.keras")

classes = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck"
]

st.title("CNN Image Classifier")
st.write("Upload a CIFAR-10 style image.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", width=250)

    image = image.resize((32,32))

    img = np.array(image)

    if img.shape[-1] == 4:
        img = img[:,:,:3]

    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    index = np.argmax(prediction)

    confidence = np.max(prediction)

    st.success(f"Prediction : {classes[index]}")

    st.write(f"Confidence : {confidence:.2%}")