from flask import Blueprint, render_template, Flask, request, session, redirect
import requests, os, datetime
from services.session_info import current_user
from models.images import create_image, find_user_image, find_image_id, update_image, delete_image, like_image, find_user_fav

NASA_API_KEY = os.environ.get("NASA_API_KEY")

home_routes = Blueprint('home_routes', __name__)

app = Flask(__name__)

def index():
    return render_template('home/index.html', current_user=current_user)

def get_image():
    response = f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}'
    data = requests.get(response).json()
    return data

def image():
    image = get_image()
    return render_template('/home/image.html', image=image, current_user=current_user)


def get_date(date):
    formatted_date = date.strftime('%Y-%m-%d')
    response = f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}&date={formatted_date}'
    data = requests.get(response).json()
    return data

def date_image():
    date_string = request.args.get('date')
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    image = get_date(date)
    return render_template('home/date_image.html', image=image, current_user=current_user)
 
def new():
    print('new')
    return render_template('/home/add_image.html', current_user=current_user)

def create():
    print('create')
    title = request.form.get('title')
    explanation = request.form.get('explanation')
    url = request.form.get('url')
    date = request.form.get('date')
    create_image(title, explanation, url, date, current_user()['id'])
    return redirect('/home/display_user_images')

def show_photos():
    user_images = find_user_image(current_user()['id'])
    return render_template('/home/display_user_images.html', user_images=user_images, current_user=current_user)

def edit(id):
    image = find_image_id(id)
    return render_template('/home/edit.html', image=image)

def update(id):
    title = request.form.get('title')
    explanation = request.form.get('explanation')
    url = request.form.get('url')
    date = request.form.get('date')
    update_image(id, title, explanation, url, date)
    return redirect('/home/display_user_images')

def delete(id):
    delete_image(id)
    return redirect ('/home/display_user_images')

# def favourite(id):
#     response = f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}'
#     data = response.json()
#     title = data['title']
#     print(data['title'])
#     explanation = data['explanation']
#     url = data['url']
#     date = data['date']
#     user_id = current_user()['id']
#     image_id = create_image(title, explanation, url, date, user_id)
#     user_favourite(title, explanation, url, date, user_id, image_id, session['user_id'])
#     return redirect('/home/image')
 
# def display_fav():
#     user_fav = find_user_fav(current_user()['id'])
#     return render_template('/home/user_fav', current_user=current_user, user_fav=user_fav)


def like(title):
    response = f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}'
    data = requests.get(response).json()
    title = data['title']
    explanation = data['explanation']
    url = data['url']
    date = data['date']
    like_image(title, explanation, url, date, session['user_id'])
    return redirect('/home/image')

def user_fav():
    fav_image = find_user_fav(session['user_id'])
    return render_template('/home/user_fav.html', current_user=current_user, fav_image=fav_image)