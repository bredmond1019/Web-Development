from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, current_app
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError

import json
import hashlib
import time
import os
from datetime import datetime, timezone

from Climbr import photos
from . import forum
from .. import db
from ..models import User, Role, Post, Permission
from .forms import PostForm, EditPostForm
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
        return redirect(url_for('forum.index'))
    post_query = Post.query.order_by(Post.timestamp.desc())
    # posts = post_query.all()
    page = request.args.get('page', 1, type=int)
    pagination = post_query.paginate(
        page, per_page=current_app.config['CLIMBR_POSTS_PER_PAGE'], error_out=False)
    posts = pagination.items
    
    return render_template('forum/forum.html', form=form, posts=posts, pagination=pagination)



@forum.route('/edit/<int:id>', methods = ['POST', 'GET'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    if current_user != post.author and \
            not current_user.can(Permission.ADMIN):
        abort(403)
    form = EditPostForm(obj = post)
    if form.validate_on_submit():
        post.body = form.body.data
        db.session.commit()
        flash("The post has been updated")
        return redirect(url_for('forum.index'))
    return render_template('forum/_edit_post.html', form=form, id=post.id)


@forum.route('/edit/<int:id>/delete', methods = ['GET','DELETE'])
@login_required
def delete(id):
    post = Post.query.get_or_404(id)
    if current_user != post.author and \
            not current_user.can(Permission.ADMIN):
        abort(403)
    if request.method == "DELETE":
        try:
            db.session.delete(post)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)
            db.session.rollback()
        finally:
            db.session.close()
        return jsonify({'success' : True })
    return render_template('forum/_delete_post.html', id=post.id)