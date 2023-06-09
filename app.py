from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import os
from flask import Flask, redirect, request
import requests
from routes.user_routes import users_routes
from routes.home_routes import home_routes
from routes.sessions_routes import sessions_routes


SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")


app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(home_routes, url_prefix='/home')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')

@app.route('/')
def index():
    return redirect('/home')
