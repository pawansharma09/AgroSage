import streamlit as st
import requests
import json
import base64
from PIL import Image
import io
import pandas as pd
from datetime import datetime, timedelta
import random
import time

# Page configuration
st.set_page_config(
    page_title="🌾 AgroSage - AI Farming Assistant",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():
    """Main application function"""
    
    # Custom CSS
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #2E8B57;
        font-size: 3rem;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: linear-gradient(45deg, #f0f8f0, #e8f5e8);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #2E8B57;
    }
    .stButton > button {
        background: linear-gradient(45deg, #2E8B57, #228B22);
        color: white;
        border: none;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">🌾 AgroSage - AI Farming Assistant</h1>', unsafe_allow_html=True)
    st.markdown("**Empowering Indian Farmers with AI-driven Agricultural Intelligence**")
    
    # Sidebar
    language, state, farm_size, farming_type = render_sidebar()
    
    # Initialize LLM Handler
    llm_handler = LLMHandler(Config.OPENROUTER_API_KEY)
    
    # Main Navigation
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "💬 Chat Assistant", 
        "📸 Pest Diagnosis", 
        "🌤️ Weather", 
        "💰 Market Prices", 
        "🏛️ Govt Schemes",
        "📚 Crop Guide"
    ])
    
    with tab1:
        render_chat_interface(llm_handler, language)
    
    with tab2:
        render_image_diagnosis()
    
    with tab3:
        render_weather_dashboard(state)
    
    with tab4:
        render_market_info()
    
    with tab5:
        render_government_schemes()
    
    with tab6:
        st.header("📚 Crop Information Guide")
        crop_name = st.selectbox("Select Crop", ["Rice", "Wheat", "Cotton", "Sugarcane"])
        
        if crop_name:
            crop_info = KnowledgeBase.get_crop_info(crop_name, state)
            
            if "message" not in crop_info:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### 🌱 Growing Information")
                    st.write(f"**Best Season:** {crop_info.get('best_season', 'N/A')}")
                    st.write(f"**Water Requirement:** {crop_info.get('water_requirement', 'N/A')}")
                    st.write(f"**Soil Type:** {crop_info.get('soil_type', 'N/A')}")
                
                with col2:
                    st.markdown("### 🧪 Fertilizer & Pests")
                    st.write(f"**Fertilizer:** {crop_info.get('fertilizer', 'N/A')}")
                    st.write("**Common Pests:**")
                    for pest in crop_info.get('pests', []):
                        st.write(f"• {pest}")
            else:
                st.warning(crop_info["message"])
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>🌾 AgroSage - Built with ❤️ for Indian Farmers</p>
        <p>📞 Helpline: 1800-180-1551 | 🌐 Digital India Initiative</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()