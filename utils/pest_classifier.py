import requests
import base64
from io import BytesIO
from PIL import Image
import streamlit as st

class PestClassifier:
    HF_API_TOKEN = st.secrets["HF_TOKEN"]
    HF_MODEL = "akhaliq/plant-disease"  # You can swap this dynamically later
    HF_API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

    @classmethod
    def classify_image(cls, image: Image.Image):
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_bytes = buffered.getvalue()

        headers = {
            "Authorization": f"Bearer {cls.HF_API_TOKEN}",
            "Content-Type": "application/octet-stream"
        }

        response = requests.post(cls.HF_API_URL, headers=headers, data=img_bytes)
        
        if response.status_code != 200:
            return {
                "name": "Unknown",
                "confidence": 0.0,
                "crop": "Unknown",
                "treatment": "Unable to determine treatment.",
                "organic_treatment": "Consider sending clearer image or contacting agri expert."
            }

        result = response.json()
        if not isinstance(result, list) or len(result) == 0:
            return {
                "name": "Unknown",
                "confidence": 0.0,
                "crop": "Unknown",
                "treatment": "Model returned no prediction.",
                "organic_treatment": "Try another image."
            }

        label = result[0]["label"]
        confidence = round(result[0]["score"] * 100, 2)

        # Basic NLP inference (dynamic mapping)
        crop = cls.extract_crop(label)
        treatment = cls.generate_treatment(label)
        organic_treatment = cls.generate_organic_treatment(label)

        return {
            "name": label,
            "confidence": confidence,
            "crop": crop,
            "treatment": treatment,
            "organic_treatment": organic_treatment
        }

    @staticmethod
    def extract_crop(label: str):
        # Try extracting crop name from label text
        known_crops = ["apple", "potato", "corn", "wheat", "grape", "tomato", "peach", "cucumber", "chili", "bell pepper"]
        for crop in known_crops:
            if crop.lower() in label.lower():
                return crop.capitalize()
        return "Unknown"

    @staticmethod
    def generate_treatment(label: str):
        if "blight" in label.lower():
            return "Use copper-based fungicides or chlorothalonil."
        elif "mildew" in label.lower():
            return "Apply sulfur or potassium bicarbonate sprays."
        elif "scab" in label.lower():
            return "Use Mancozeb; prune affected leaves."
        elif "healthy" in label.lower():
            return "No treatment needed. Keep monitoring."
        else:
            return "Use general antifungal spray or consult an expert."

    @staticmethod
    def generate_organic_treatment(label: str):
        if "blight" in label.lower():
            return "Use neem oil or garlic-chili spray."
        elif "mildew" in label.lower():
            return "Spray diluted milk or baking soda solution."
        elif "scab" in label.lower():
            return "Apply compost tea or sulfur dust."
        elif "healthy" in label.lower():
            return "No action needed."
        else:
            return "Try neem oil or compost-based foliar spray."
