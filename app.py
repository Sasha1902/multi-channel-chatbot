# app.py
from flask import Flask, render_template, request, jsonify
from services import get_weather, book_appointment

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.json.get("city")
    result = get_weather(city)
    return jsonify({"response": result})

@app.route("/appointment", methods=["POST"])
def appointment():
    date = request.json.get("date")
    time = request.json.get("time")
    result = book_appointment(date, time)
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(debug=True)