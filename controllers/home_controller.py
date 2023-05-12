from flask import Blueprint, render_template, Flask
import requests
from services.session_info import current_user
home_routes = Blueprint('home_routes', __name__)

app = Flask(__name__)

@home_routes.route('/')
def index():
    return render_template('home/index.html', current_user=current_user)


@home_routes.route('/')
def result():
    print('https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}')
    response = 'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}'
    print(response.content)
    data = requests.get(response).json()
    return render_template('index.html', data=data)