# 🌾 AgroSage - AI Farming Assistant

## Overview
AgroSage is a comprehensive AI-powered agricultural assistant designed specifically for Indian farmers. It provides multilingual support, crop guidance, pest diagnosis, weather forecasts, and market information.

## Features
- **Multilingual Chat Assistant**: Get farming advice in 6 Indian languages
- **Image-based Pest Diagnosis**: Upload crop images for AI-powered pest/disease identification
- **Weather-based Recommendations**: 5-day weather forecast with farming advice
- **Market Price Information**: Real-time crop pricing and alerts
- **Government Schemes**: Information about farming subsidies and benefits
- **Crop Knowledge Base**: Detailed information about major Indian crops

## Tech Stack
- **Frontend**: Streamlit
- **LLM**: OpenRouter API (Mistral-7B-Instruct)
- **Image Processing**: PIL (Pillow)
- **Data Processing**: Pandas
- **Deployment**: Streamlit Cloud

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd agrosage
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   - Create `.streamlit/secrets.toml`
   - Add your OpenRouter API key:
     ```toml
     OPENROUTER_API_KEY = "your_api_key_here"
     ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Deployment on Streamlit Cloud

1. Push your code to GitHub
2. Connect your GitHub repo to Streamlit Cloud
3. Add your OpenRouter API key in the Streamlit Cloud secrets
4. Deploy!

## Features for Resume/Demo
- **Multilingual AI Assistant**: Showcases NLP and localization skills
- **Computer Vision**: Image-based pest diagnosis
- **API Integration**: OpenRouter LLM integration
- **Data Visualization**: Weather and market data dashboards
- **User Experience**: Clean, mobile-friendly interface
- **Production Ready**: Error handling, configuration management

## Future Enhancements
- Real-time market data integration
- Advanced CNN model for pest classification
- Voice input/output capabilities
- Offline mode with cached responses
- Integration with government APIs

## Contact
Built with ❤️ for Indian Farmers
By Pawan Sharma