import streamlit as st

def render_chat_interface(llm_handler, language):
    """Render chat interface"""
    st.header("💬 Ask AgroSage")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Chat input
    user_input = st.chat_input("Ask your farming question...")
    
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get AI response
        with st.spinner("AgroSage is thinking..."):
            response = llm_handler.get_response(user_input, language)
        
        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
