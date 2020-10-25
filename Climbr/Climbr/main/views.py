# from Climbr import app
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError

from . import main
from .. import db
from ..models import User, Role
from .forms import EditProfileForm, EditClimbingForm, EditProfileAdminForm
from ..decorators import admin_required



@main.route('/', methods=['GET', 'POST'])
def index():


    return render_template('home.html')

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

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
    return render_template('edit_profile.html', form=form)


@main.route('/user/<username>/edit-climbing', methods=['GET', 'POST'])
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
    return render_template('edit_climbing.html', form=form)


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
    return render_template('edit_profile_admin.html', form=form, user=user)