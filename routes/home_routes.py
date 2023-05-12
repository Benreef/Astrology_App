from flask import Blueprint
from controllers.home_controller import index, image, get_image, date_image

home_routes = Blueprint('home_routes', __name__)


home_routes.route('/')(index)
home_routes.route('/image')(image)
home_routes.route('/get_image')(get_image)
home_routes.route('/date_image')(date_image)
