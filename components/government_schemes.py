import streamlit as st
from utils.knowledge_base import KnowledgeBase

def render_government_schemes():
    """Render government schemes information"""
    st.header("🏛️ Government Schemes")

    schemes = KnowledgeBase.get_government_schemes()

    for scheme in schemes:
        with st.expander(f"📋 {scheme['name']}"):
            st.write(f"**Description:** {scheme['description']}")
            st.write(f"**Eligibility:** {scheme['eligibility']}")
            st.markdown(f"[🔗 Apply for {scheme['name']}]({scheme['url']})", unsafe_allow_html=True)
