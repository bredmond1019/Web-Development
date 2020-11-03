from flask import Blueprint

partner = Blueprint('partner', __name__)

from . import views
