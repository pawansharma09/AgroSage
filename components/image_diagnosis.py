import time
import streamlit as st
from PIL import Image
from utils.pest_classifier import PestClassifier

def render_image_diagnosis():
    """Render image diagnosis interface"""
    st.header("📸 Pest & Disease Diagnosis")
    
    uploaded_file = st.file_uploader(
        "Upload crop/leaf image for diagnosis",
        type=['png', 'jpg', 'jpeg'],
        help="Take a clear photo of affected plant parts"
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(image, caption="Uploaded Image", use_column_width=True)
        
        with col2:
            with st.spinner("Analyzing image..."):
                # Simulate analysis delay
                time.sleep(2)
                
                # Get classification result
                result = PestClassifier.classify_image(image)
                
                st.success(f"**Detected:** {result['name']}")
                st.info(f"**Confidence:** {result['confidence']:.0%}")
                st.write(f"**Affected Crop:** {result['crop']}")
                
                st.markdown("### 💊 Treatment Recommendations")
                st.write(f"**Chemical:** {result['treatment']}")
                st.write(f"**Organic:** {result['organic_treatment']}")
                
                # Additional advice
                st.markdown("### 📋 Additional Advice")
                st.write("• Apply treatment during early morning or evening")
                st.write("• Maintain proper field sanitation")
                st.write("• Monitor regularly for re-infestation")
