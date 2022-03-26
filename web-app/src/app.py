import json
from os import getenv
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify("API is running")

@app.route("/city/<string:city>")
def city(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={getenv('key')}&lang=pt_br"
    req = requests.get(url)

    return json.loads(req.content)

@app.route("/state/<string:state>")
def state(state):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={state}&appid={getenv('key')}&lang=pt_br"
    req = requests.get(url)

    return json.loads(req.content)

@app.route("/coordinates/<string:lat>/<string:lon>")
def coordinates(lat,lon):

    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={getenv('key')}&units=metric&lang=pt_br"
    req = requests.get(url)

    return json.loads(req.content)

if __name__ == "__main__":
    app.run()
