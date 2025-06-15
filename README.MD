# Weather & Mood Recommendation App 🌤️🧠🎧

## 📌 Description

This Python application helps users get personalized activity or self-care recommendations based on two factors:
1. **Current weather** in their city (via OpenWeatherMap API)
2. **User's mood**, detected via sentiment analysis (using NLTK)

It's a smart, simple command-line tool that combines external API use, machine learning, clean modular code, and testing.

---

## 🚀 Features

- ✅ Live weather data using OpenWeatherMap API
- ✅ Mood detection using VADER sentiment analysis
- ✅ Personalized recommendation engine
- ✅ Modular code with classes and functions
- ✅ Unit testing with `pytest`
- ✅ Error and exception handling
- ✅ Readable code with list comprehensions and standard library usage

---

## 📦 Project Structure

```
dsw_proj/
│
├── main.py                      # Entry point of the app
├── weather_api.py               # Fetches weather data
├── mood_analyzer.py             # Analyzes sentiment of user input
├── recommendation.py            # Suggests an activity based on weather + mood
├── requirements.txt             # Project dependencies
│
├── tests/
│   ├── __init__.py
│   └── test_mood_analyzer.py    # Unit tests for sentiment logic
└── __init__.py
```

---

## 🧪 Technologies

- Python 3.10+
- [OpenWeatherMap API](https://openweathermap.org/current)
- `nltk` (for sentiment analysis)
- `requests` (for API calls)
- `pytest` (for testing)

---

## 🛠️ Installation

1. **Clone the repo:**

```bash
git clone https://github.com/yourusername/weather-mood-app.git
cd weather-mood-app
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set up your OpenWeatherMap API key:**

Edit `weather_api.py` and replace:

```python
self.apiKey = "your_api_key_here"
```

with your actual API key from [openweathermap.org](https://home.openweathermap.org/api_keys).

---

## ▶️ How to Run

```bash
python main.py
```

Example usage:

```
Enter your city: Wroclaw
How are you feeling today?: I'm tired but hopeful.

Weather in Wroclaw:
- Condition: clear (clear sky)
- Temperature: 21.5°C
- Humidity: 40%
- Wind Speed: 2.6 m/s

Recommendation: Go for a run or have a picnic in the park!
```

---

## 🧪 Run Unit Tests

```bash
pytest
```

This runs tests in `tests/test_mood_analyzer.py`.

---

## 💡 Possible Improvements

- Add GUI using `tkinter` or `PyQt`
- Telegram bot version
- Save weather/mood history to file
- Add music playlist integration (e.g. Spotify API)
- Use emojis/icons for weather and mood

---
