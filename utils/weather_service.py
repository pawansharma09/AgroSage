class WeatherService:
    """Simulated weather service"""
    
    @staticmethod
    def get_weather_forecast(state):
        """Get weather forecast for farming decisions"""
        weather_conditions = ["Sunny", "Partly Cloudy", "Rainy", "Thunderstorm"]
        forecast = []
        
        for i in range(5):
            date = datetime.now() + timedelta(days=i)
            forecast.append({
                "date": date.strftime("%Y-%m-%d"),
                "condition": random.choice(weather_conditions),
                "temp_max": random.randint(25, 40),
                "temp_min": random.randint(15, 25),
                "humidity": random.randint(40, 90),
                "rainfall": random.randint(0, 50) if random.choice([True, False]) else 0
            })
        
        return forecast
    
    @staticmethod
    def get_farming_advice(forecast):
        """Get farming advice based on weather"""
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
