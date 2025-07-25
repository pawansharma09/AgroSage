import streamlit as st
from utils.weather_service import WeatherService

def render_weather_dashboard():
    """Render dynamic weather dashboard"""
    st.title("🌦️ Real-Time Weather & Farming Insights")

    city = st.text_input("Enter your city or state name:", "Delhi")
    api_key = st.secrets["weather_api_key"]

    if city:
        try:
            forecast = WeatherService.get_weather_forecast(city, api_key)
            advice = WeatherService.get_farming_advice(forecast)

            st.header(f"🌤️ Weather Forecast - {city}")
            cols = st.columns(5)
            for i, day in enumerate(forecast):
                with cols[i]:
                    st.metric(
                        label=day["date"],
                        value=f"{day['temp_max']}°C",
                        delta=f"{day['temp_min']}°C min"
                    )
                    st.write(f"🌧️ {day['rainfall']} mm")
                    st.write(f"💧 {day['humidity']}% RH")
                    st.write(f"🌤️ {day['condition']}")

            st.markdown("### 🌾 Weather-based Farming Advice")
            for i, tip in enumerate(advice):
                st.write(f"{i+1}. {tip}")

        except ValueError as e:
            st.error(str(e))
