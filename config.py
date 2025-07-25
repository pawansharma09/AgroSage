import streamlit as st

class Config:
    # OpenRouter API Configuration
    OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY", "")
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
    
    # Model Configuration
    MODEL_NAME = "mistralai/mistral-7b-instruct:free"
    
    # Supported Languages
    LANGUAGES = {
        "English": "en",
        "हिंदी (Hindi)": "hi",
        "मराठी (Marathi)": "mr",
        "தமிழ் (Tamil)": "ta",
        "বাংলা (Bengali)": "bn",
        "ગુજરાતી (Gujarati)": "gu"
    }
    
    # Indian States for Weather
    STATES = [
        "Andhra Pradesh", "Bihar", "Gujarat", "Haryana", "Karnataka",
        "Madhya Pradesh", "Maharashtra", "Punjab", "Rajasthan", "Tamil Nadu",
        "Uttar Pradesh", "West Bengal"
    ]
