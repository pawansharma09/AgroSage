import requests
import random
import streamlit as st
from datetime import datetime, timedelta

class WeatherService:
    """Live weather service using OpenWeatherMap API"""

    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

    @staticmethod
    def get_weather_forecast(state):
        """Get real 5-day forecast using OpenWeatherMap"""
        api_key = st.secrets["weather_api_key"]  # Uses existing secrets setup
        params = {
            "q": state,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(WeatherService.BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200 or "list" not in data:
            raise ValueError(f"Weather API error: {data.get('message', 'Unknown error')}")

        forecast = []
        used_dates = set()

        for entry in data["list"]:
            dt_txt = entry["dt_txt"]
            date_only = dt_txt.split(" ")[0]
            time_only = dt_txt.split(" ")[1]

            # Only one reading per day, ideally around midday
            if date_only not in used_dates and time_only.startswith("12"):
                forecast.append({
                    "date": date_only,
                    "condition": entry["weather"][0]["main"],
                    "temp_max": round(entry["main"]["temp_max"]),
                    "temp_min": round(entry["main"]["temp_min"]),
                    "humidity": entry["main"]["humidity"],
                    "rainfall": entry.get("rain", {}).get("3h", 0)
                })
                used_dates.add(date_only)

            if len(forecast) >= 5:
                break

        return forecast

    @staticmethod
    def get_farming_advice(forecast):
        """Get farming advice based on live forecast"""
        advice = []

        for day in forecast:
            if day["rainfall"] > 20:
                advice.append("Heavy rainfall expected. Avoid spraying pesticides.")
            elif day["temp_max"] > 35:
                advice.append("High temperature. Increase irrigation frequency.")
            elif day["humidity"] > 80:
                advice.append("High humidity. Monitor for fungal diseases.")
            else:
                advice.append("Good weather for field operations.")

        return advice
