import streamlit as st

class Config:
    # OpenRouter API Configuration
    OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY", "")
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
    
    # Model Configuration
    MODEL_NAME = "mistralai/mistral-7b-instruct:free"
    
    # Top 10 Most Spoken Languages in India (with ISO codes)
    LANGUAGES = {
        "English": "en",
        "हिंदी (Hindi)": "hi",
        "বাংলা (Bengali)": "bn",
        "తెలుగు (Telugu)": "te",
        "मराठी (Marathi)": "mr",
        "தமிழ் (Tamil)": "ta",
        "ગુજરાતી (Gujarati)": "gu",
        "उर्दू (Urdu)": "ur",
        "ಕನ್ನಡ (Kannada)": "kn",
        "ओड़िया (Odia)": "or",
        "മലയാളം (Malayalam)": "ml"
    }

    # All States and Union Territories of India
    STATES = [
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
        "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
        "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
        "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
        "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
        "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
        "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
    ]
