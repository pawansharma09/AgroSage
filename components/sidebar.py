from config import Config
import streamlit as st

def render_sidebar():
    """Render sidebar with user preferences"""
    st.sidebar.title("🌾 AgroSage Settings")
    
    # Language Selection
    selected_language = st.sidebar.selectbox(
        "🗣️ Select Language",
        list(Config.LANGUAGES.keys()),
        index=0
    )
    
    # State Selection
    selected_state = st.sidebar.selectbox(
        "📍 Select State",
        Config.STATES,
        index=5  # Default to Madhya Pradesh
    )
    
    # User Profile
    st.sidebar.markdown("---")
    st.sidebar.markdown("👨‍🌾 **Farmer Profile**")
    farm_size = st.sidebar.slider("Farm Size (acres)", 1, 100, 5)
    farming_type = st.sidebar.radio("Farming Type", ["Organic", "Conventional", "Mixed"])
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("📱 **Quick Actions**")
    if st.sidebar.button("🆘 Emergency Helpline"):
        st.sidebar.success("Kisan Call Center: 1800-180-1551")
    
    return selected_language, selected_state, farm_size, farming_type
