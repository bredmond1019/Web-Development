from flask import Blueprint

forum = Blueprint('forum', __name__)

from . import views
from ..models import Permission

@forum.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)