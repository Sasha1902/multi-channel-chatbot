# services.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # .env laden

OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")

def get_weather(city):
    """Ruft Wetterinformationen von OpenWeatherMap ab."""
    if not OPENWEATHER_KEY:
        return "OpenWeatherMap Key fehlt!"
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric&lang=de"
    r = requests.get(url)
    data = r.json()

    if r.status_code != 200:
        return "Stadt nicht gefunden."

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"Wetter in {city}: {temp}°C, {desc}"

def book_appointment(date, time):
    """Fiktive Terminbuchung"""
    return f"Termin bestätigt für {date} um {time}."