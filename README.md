
# Multi-Channel Chatbot
=======

## Beschreibung

Dies ist ein Multi-Channel Chatbot, der sowohl über **Telegram** als auch über eine einfache **Webanwendung** erreichbar ist.  
Der Bot kann:

- Wetterinformationen für eine angegebene Stadt abrufen (OpenWeatherMap API)  
- Fiktive Terminbuchungen bestätigen  

Die Webanwendung verwendet **Flask** mit **AJAX**, um Anfragen ohne Neuladen der Seite zu bearbeiten.

---

## Installation

1. Repository klonen oder Projektordner auf den PC kopieren.
2. Virtuelle Umgebung erstellen:

```bash
python -m venv venv

python app.py
python telegram_bot.py
=======
