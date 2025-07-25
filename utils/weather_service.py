import requests
from datetime import datetime, timedelta

class WeatherService:
    """Live weather service using OpenWeatherMap API"""

    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

    @staticmethod
    def get_weather_forecast(city_name, api_key):
        """Fetch 5-day forecast from OpenWeatherMap"""
        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(WeatherService.BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200 or "list" not in data:
            raise ValueError(f"Failed to fetch data: {data.get('message', 'Unknown error')}")

        # Process forecast for next 5 days at 12:00 PM
        forecast_map = {}
        for entry in data["list"]:
            dt_txt = entry["dt_txt"]
            if "12:00:00" in dt_txt:
                date = dt_txt.split(" ")[0]
                forecast_map[date] = {
                    "date": date,
                    "condition": entry["weather"][0]["main"],
                    "temp_max": round(entry["main"]["temp_max"]),
                    "temp_min": round(entry["main"]["temp_min"]),
                    "humidity": entry["main"]["humidity"],
                    "rainfall": entry.get("rain", {}).get("3h", 0)
                }

        return list(forecast_map.values())[:5]

    @staticmethod
    def get_farming_advice(forecast):
        """Generate farming advice based on weather"""
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
