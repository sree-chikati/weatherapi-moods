import requests
import datetime
import os

from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
from datetime import datetime


#-------- Setup --------#
app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('API_KEY')

#-------- Routes --------#
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/results')
def results():
    # URL it gets the info from:
    url = 'http://api.openweathermap.org/data/2.5/weather'

    # parameters
    city = request.args.get('city')
    units = request.args.get('units')
    mood = request.args.get('mood')

    params = {
        "appid": API_KEY, 
        "q": city,
        "units": units,
    }

    result_json = requests.get(url, params=params).json()

    context = {
        'date': datetime.now(),
        'city': city,
        'temp_units': temp_units(units),
        'mood': mood,
        'description': result_json['weather'][0]['description'],
        'temp': result_json['main']['temp']
    }

    return render_template('results.html', **context)

@app.route('/mood')
def mood():
    # parameters
    mood = request.args.get('mood')

    context = {
        'mood': mood
    }

    return render_template('mood.html', **context)

def temp_units(units):
    if units == 'imperial':
        return 'F'
    else: 
        return "C"

if __name__ == '__main__':
    app.run(debug=True)