from flask import Blueprint

profiles_bp = Blueprint('profiles', __name__)

from backend.controllers.profiles import views