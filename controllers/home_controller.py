from flask import Blueprint, render_template, Flask
import requests, os
from services.session_info import current_user
SECRET_KEY = os.environ.get("NASA_API_KEY")
home_routes = Blueprint('home_routes', __name__)

app = Flask(__name__)

@home_routes.route('/')
def index():
    print('running')
    return render_template('home/index.html', current_user=current_user)

@home_routes.route('/get_image')
def get_image():
    response = f'https://api.nasa.gov/planetary/apod?api_key={SECRET_KEY}'
    data = requests.get(response).json()
    print(data)
    return data

@home_routes.route('/image')
def image():
    print('mew')
    image = get_image()
    return render_template('/home/image.html', image=image, current_user=current_user)

