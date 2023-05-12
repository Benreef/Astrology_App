from flask import Blueprint
from controllers.home_controller import index, result

home_routes = Blueprint('home_routes', __name__)


home_routes.route('/')(index)
home_routes.route('/')(result)