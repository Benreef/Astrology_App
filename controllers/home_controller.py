from flask import Blueprint, render_template, Flask, request, session
import requests, os, datetime
from services.session_info import current_user
SECRET_KEY = os.environ.get("NASA_API_KEY")
home_routes = Blueprint('home_routes', __name__)

app = Flask(__name__)

def index():
    print('running')
    return render_template('home/index.html', current_user=current_user)

def get_image():
    response = f'https://api.nasa.gov/planetary/apod?api_key={SECRET_KEY}'
    data = requests.get(response).json()
    return data

def image():
    image = get_image()
    return render_template('/home/image.html', image=image, current_user=current_user)


def get_date(date):
    print('hello')
    formatted_date = date.strftime('%Y-%m-%d')
    response = f'https://api.nasa.gov/planetary/apod?api_key={SECRET_KEY}&date={formatted_date}'
    print(formatted_date)
    data = requests.get(response).json()
    return data

def date_image():
    print("hello")
    date_string = request.args.get('date')
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    image = get_date(date)
    return render_template('home/date_image.html', image=image, current_user=current_user)
 