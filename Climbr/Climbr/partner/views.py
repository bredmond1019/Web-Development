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
    users = User.query.all()
    return render_template('partner/partner.html', users=users)