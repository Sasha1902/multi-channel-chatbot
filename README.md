# multi-channel-chatbot

## Beschreibung

Dies ist ein Multi-Channel Chatbot, der sowohl über **Telegram** als auch über eine einfache **Webanwendung** erreichbar ist.  
Der Bot kann:

- Wetterinformationen für eine angegebene Stadt abrufen (OpenWeatherMap API)  
- Fiktive Terminbuchungen bestätigen  

Die Webanwendung verwendet **Flask** mit **AJAX**, um Anfragen ohne Neuladen der Seite zu bearbeiten.

---
## Projektstruktur
multi-channel-chatbot/
│
├─ telegram_bot.py # Telegram Bot
├─ app.py # Flask Web-App
├─ services.py # Funktionen für Wetter & Termin
├─ requirements.txt # Python-Abhängigkeiten
├─ .env.example # Platzhalter für Tokens
├─ README.md # Diese Datei
│
├─ templates/
│ └─ index.html
└─ static/
├─ style.css
└─ script.js
---
