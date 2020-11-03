from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, current_app
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError

import hashlib
import time
import os
from datetime import datetime, timezone

from Climbr import photos
from . import forum
from .. import db
from ..models import User, Role, Post, Permission
from .forms import PostForm
from ..decorators import admin_required


'''
Forum
'''
@forum.route('/', methods = ['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE) and form.validate_on_submit():
        try:
            post = Post(body=form.body.data,
                        author=current_user._get_current_object(),
                        timestamp = datetime.now(tz = timezone.utc))
            db.session.add(post)
            db.session.commit()
            flash("Your post was successfully added!")
        except SQLAlchemyError as e:
            print(e)
            flash("There was an error while attempting to post. Please try again later")
            db.session.rollback()
        finally:
            db.session.close()
        return redirect(url_for('main.forum'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    
    return render_template('forum/forum.html', form=form, posts=posts)
