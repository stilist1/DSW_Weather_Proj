from weather_api import WeatherClient
from mood_analyzer import MoodAnalyzer
from recommendation import getRecommendation


def main():
    print("Welcome to the Weather & Mood Recommendation App")
    weatherClient = WeatherClient()

    while True:
        city = input("Enter your city: ")
        try:
            weatherData = weatherClient.getCurrentWeather(city)
            break  
        except Exception as error:
            print(f"An error occurred: {error}")
            print("Please try again.\n")

    userInput = input("How are you feeling today?: ")
    moodAnalyzer = MoodAnalyzer()
    mood = moodAnalyzer.analyzeMood(userInput)

    print(f"\nWeather in {city}:")
    print(f"- Condition: {weatherData['main']} ({weatherData['description']})")
    print(f"- Temperature: {weatherData['temperature']}°C")
    print(f"- Humidity: {weatherData['humidity']}%")
    print(f"- Wind Speed: {weatherData['windSpeed']} m/s")

    suggestion = getRecommendation(weatherData['main'], mood)
    print(f"\nRecommendation: {suggestion}")


if __name__ == "__main__":
    main()
