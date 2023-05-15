from flask import Blueprint
from controllers.home_controller import index, image, get_image, date_image, new, create, show_photos, edit, update, delete

home_routes = Blueprint('home_routes', __name__)


home_routes.route('/')(index)
home_routes.route('/image')(image)
home_routes.route('/get_image')(get_image)
home_routes.route('/date_image')(date_image)
home_routes.route('/add_image')(new)
home_routes.route('/user_image', methods=["POST"])(create)
home_routes.route('/display_user_images')(show_photos)
home_routes.route('/<id>/edit')(edit)
home_routes.route('/<id>', methods=["POST"])(update)
home_routes.route('/<id>/delete', methods=["POST"])(delete)