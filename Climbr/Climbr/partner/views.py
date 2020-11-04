from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, current_app
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError

import hashlib
import time
import os
from datetime import datetime, timezone

from . import partner
from .. import db
from ..models import User, Role, Post, Permission
from ..decorators import admin_required

@partner.route('/', methods = ['GET', 'POST'])
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.order_by(User.last_seen.desc()).paginate(
        page, per_page=current_app.config['CLIMBR_POSTS_PER_PAGE'], error_out=False
    )
    users = pagination.items
    return render_template('partner/partner.html', users=users, pagination=pagination)

    