# from Climbr import app

from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, current_app
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError

import hashlib
import time
import os
from datetime import datetime, timezone

from Climbr import photos
from . import main
from .. import db
from ..models import User, Role, Post, Permission
from .forms import EditProfileForm, EditClimbingForm, EditProfileAdminForm, ProfilePicForm
from ..decorators import admin_required


'''
Home Page
'''
@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')






'''
User's Page
'''
@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    app = current_app._get_current_object()
    if user.photo_url:
        photo_url = user.photo_url
    else:
        photo_url = ''
    return render_template('user/user.html', user=user, photo_url=photo_url)


@main.route('/user/<username>/upload-photo', methods=['GET', 'POST'])
@login_required
def upload_photo(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = ProfilePicForm()
    if form.validate_on_submit():
        for filename in request.files.getlist('photo'):
            name = hashlib.md5(user.email.lower().encode('utf-8')).hexdigest()
            print(name)
            photos.save(filename, name=f'{name}.')
        try:
            setattr(user, 'photo_url', f'uploads/{name}.jpg')
            db.session.commit()
            flash("Photo successfully uploaded")
        except SQLAlchemyError as e:
            print(e)
            flash("Something went wrong while trying to upload the file. \
                Please try again or choose a different file.")
            db.session.rollback()
        finally:
            db.session.close
            return  redirect(url_for('main.user', username=current_user.username))
    return render_template('user/upload_photo.html', form=form)





@main.route('/user/<username>/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EditProfileForm(obj = user)
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        try:
            for key in request.form:
                setattr(user, key, request.form[key])
            db.session.commit()
            flash(f"Alright, {user.first_name}, you've successfully update your profile")
        except SQLAlchemyError as e:
            print(e)
            flash('Sorry, there was an error while updating your profile. \
                  Please make sure all of the information is correct then submit again')
            db.session.rollback()
        finally:
            db.session.close()
            return redirect(url_for('main.user', username=current_user.username))
    return render_template('user/edit_profile.html', form=form)


@main.route('/user/<username>/edit-climbing', methods=['GET', 'POST'])
@login_required
def edit_climbing(username):
    user = User.query.filter_by(username=username).first_or_404() 
    form = EditClimbingForm(obj = user)
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        try:
            for key in request.form:
                setattr(user, key, request.form[key])
            db.session.commit()
            flash(f"Alright, {user.first_name}, you've successfully update your profile")
        except SQLAlchemyError as e:
            print(e)
            flash('Sorry, there was an error while updating your profile. \
                  Please make sure all of the information is correct then submit again')
            db.session.rollback()
        finally:
            db.session.close()
            return redirect(url_for('main.user', username=current_user.username))
    return render_template('user/edit_climbing.html', form=form)


@main.route('/edit-profile/<int:id>', methods = ['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user, obj = user)
    print(request.form)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        try:
            for key in request.form:
                if key == 'confirmed':
                    setattr(user, key, True if request.form[key]=='y' else False)
                elif key == 'role':
                    setattr(user, key, Role.query.get(int(request.form[key])))
                else:
                    setattr(user, key, request.form[key])
            db.session.commit()
            flash(f"Alright, {current_user.first_name}, you've successfully updated {user.first_name}'s profile")
        except SQLAlchemyError as e:
            print(e)
            flash('Sorry, there was an error while updating your profile. \
                  Please make sure all of the information is correct then submit again')
            db.session.rollback()
        finally:
            db.session.close()
        return redirect(url_for('main.user', username=user.username))
    return render_template('user/edit_profile_admin.html', form=form, user=user)






'''
Find Partner
'''














'''
Forum
'''
# @main.route('/forum', methods = ['GET', 'POST'])
# @login_required
# def forum():
#     form = PostForm()
#     if current_user.can(Permission.WRITE) and form.validate_on_submit():
#         try:
#             post = Post(body=form.body.data,
#                         author=current_user._get_current_object(),
#                         timestamp = datetime.now(tz = timezone.utc))
#             db.session.add(post)
#             db.session.commit()
#             flash("Your post was successfully added!")
#         except SQLAlchemyError as e:
#             print(e)
#             flash("There was an error while attempting to post. Please try again later")
#             db.session.rollback()
#         finally:
#             db.session.close()
#         return redirect(url_for('main.forum'))
#     posts = Post.query.order_by(Post.timestamp.desc()).all()
    
#     return render_template('forum/forum.html', form=form, posts=posts)
