import requests
import base64
import streamlit as st

class PestClassifier:
    HF_API_URL = "https://api-inference.huggingface.co/models/Amrrs/plant_disease"
    HF_TOKEN = st.secrets["HF_TOKEN"]

    @classmethod
    def classify_image(cls, image):
        # Convert PIL image to base64
        buffered = image.convert("RGB")
        buffered.save("temp.jpg", format="JPEG")
        with open("temp.jpg", "rb") as img_file:
            img_bytes = img_file.read()

        headers = {
            "Authorization": f"Bearer {cls.HF_TOKEN}",
            "Content-Type": "application/octet-stream"
        }

        response = requests.post(cls.HF_API_URL, headers=headers, data=img_bytes)

        if response.status_code != 200:
            return {
                "name": "Unknown Pest",
                "confidence": 0.0,
                "crop": "N/A",
                "treatment": "N/A",
                "organic_treatment": "N/A"
            }

        predictions = response.json()
        top_result = predictions[0] if predictions else {"label": "Unknown", "score": 0.0}

        # For now we use hardcoded values for crop and treatment
        # In a production version, you can map results['label'] to actual pest DB
        return {
            "name": top_result['label'],
            "confidence": top_result['score'],
            "crop": "Tomato" if "Tomato" in top_result['label'] else "Unknown",
            "treatment": "Use Imidacloprid 17.8 SL" if "blight" in top_result['label'].lower() else "Consult agronomist",
            "organic_treatment": "Neem oil spray"
        }
