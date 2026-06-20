import json
from pathlib import Path

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image


# ==================================================
# Paths
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "final_tomato_disease_model.keras"
CLASS_NAMES_PATH = BASE_DIR / "model" / "class_names.json"

IMG_SIZE = (224, 224)


# ==================================================
# Load Model
# ==================================================

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


@st.cache_data
def load_class_names():
    with open(CLASS_NAMES_PATH, "r") as file:
        return json.load(file)


# ==================================================
# Image Preprocessing
# ==================================================

def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize(IMG_SIZE)

    image_array = np.array(image).astype("float32")
    image_array = np.expand_dims(image_array, axis=0)

    return image_array


def predict_disease(image, model, class_names): 
    processed_image = preprocess_image(image)

    predictions = model.predict(processed_image)[0]

    predicted_index = np.argmax(predictions)
    predicted_class = class_names[predicted_index]
    confidence = predictions[predicted_index] * 100

    return predicted_class, confidence

# ==================================================
# Disease Information
# ==================================================

disease_info = {
    "Tomato__Bacterial_Spot":
        "Bacterial Spot is caused by bacteria and appears as small dark lesions on leaves.",

    "Tomato__Early_Blight":
        "Early Blight causes concentric brown rings on leaves and stems.",

    "Tomato__Healthy":
        "The tomato leaf appears healthy with no visible disease symptoms.",

    "Tomato__Late_Blight":
        "Late Blight causes water-soaked lesions and rapid plant deterioration.",

    "Tomato__Leaf_Mold":
        "Leaf Mold appears as yellow spots on upper leaf surfaces with mold underneath.",

    "Tomato__Mosaic_Virus":
        "Mosaic Virus causes mottled leaf coloration and distorted growth.",

    "Tomato__Septoria_Leaf_Spot":
        "Septoria Leaf Spot causes numerous small circular lesions on leaves.",

    "Tomato__Target_Spot":
        "Target Spot produces circular lesions with concentric rings.",

    "Tomato__Two_Spotted_Spider_Mites":
        "Spider Mites cause yellow stippling and leaf damage due to feeding.",

    "Tomato__YellowLeaf_Curl_Virus":
        "Yellow Leaf Curl Virus causes upward leaf curling and yellowing."
}


# ==================================================
# App UI
# ==================================================

st.set_page_config(
    page_title="Tomato Disease Detection",
    page_icon="🍅",
    layout="centered"
)

st.title("🍅 Tomato Disease Detection")

st.caption(
    "Deep Learning Based Tomato Leaf Disease Classification Using MobileNetV2"
)

# ==================================================
# Load Resources
# ==================================================

model = load_model()
class_names = load_class_names()

# ==================================================
# File Upload
# ==================================================

uploaded_file = st.file_uploader(
    "Choose a tomato leaf image",
    type=["jpg", "jpeg", "png"]
)

# ==================================================
# Prediction
# ==================================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Leaf Image",
        use_container_width=True
    )

    if st.button("Predict Disease"):

        predicted_class, confidence = predict_disease(image, model, class_names)

        clean_name = (
            predicted_class
            .replace("Tomato__", "")
            .replace("_", " ")
        )

        if(clean_name == "Healthy"):
            st.success(
                f'Plant is Healthy, No disease detected' 
            )
        else:
            st.success(
                f"Predicted Disease: {clean_name}"
            )

        st.info(
            f"Confidence: {confidence:.2f}%"
        )

        st.subheader("Disease Information")

        st.write(
            disease_info.get(
                predicted_class,
                "Information not available."
            )
        )

        # st.subheader("Top 3 Predictions")

        # top_indices = np.argsort(predictions)[::-1][:3]

        # for idx in top_indices:

        #     disease_name = (
        #         class_names[idx]
        #         .replace("Tomato__", "")
        #         .replace("_", " ")
        #     )

        #     st.write(
        #         f"**{disease_name}** : {predictions[idx] * 100:.2f}%"
        #     )