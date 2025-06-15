import requests

class WeatherClient:
    def __init__(self):
        self.apiKey = "0a50c277fad1965074f26531a744aa94"  # ← свой ключ
        self.baseUrl = "https://api.openweathermap.org/data/2.5/weather"

    def getCurrentWeather(self, cityName):
        params = {
            "q": cityName,
            "appid": self.apiKey,
            "units": "metric"
        }
        response = requests.get(self.baseUrl, params=params)

        if response.status_code != 200:
            try:
                errorMessage = response.json().get('message', 'Unknown error')
            except Exception:
                errorMessage = 'Unknown error'
            raise Exception(f"Weather API request failed: {errorMessage}")

        data = response.json()

        weatherInfo = {
            "main": data["weather"][0]["main"].lower(),
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "windSpeed": data["wind"]["speed"]
        }

        return weatherInfo
