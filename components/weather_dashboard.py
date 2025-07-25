import streamlit as st
from utils.weather_service import WeatherService

def render_weather_dashboard(state):
    """Render weather dashboard"""
    st.header(f"🌤️ Weather Forecast - {state}")
    
    # Get weather data
    forecast = WeatherService.get_weather_forecast(state)
    advice = WeatherService.get_farming_advice(forecast)
    
    # Display forecast
    cols = st.columns(5)
    for i, day in enumerate(forecast):
        with cols[i]:
            st.metric(
                label=day["date"],
                value=f"{day['temp_max']}°C",
                delta=f"{day['temp_min']}°C min"
            )
            st.write(f"🌧️ {day['rainfall']}mm")
            st.write(f"💧 {day['humidity']}% RH")
    
    # Farming advice
    st.markdown("### 🌾 Weather-based Farming Advice")
    for i, tip in enumerate(advice):
        st.write(f"{i+1}. {tip}")
