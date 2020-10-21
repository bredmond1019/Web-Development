from flask import render_template, redirect, url_for, flash, request, Response, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from Climbr import db
from . import auth
from .forms import SignUpForm, LoginForm
from ..models import User
from ..email import send_email

from sqlalchemy.exc import SQLAlchemyError




@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    print(request.form)
    if form.validate_on_submit():
        try:
            user = User(first_name = form.first_name.data,
                        last_name = form.last_name.data,
                        age = form.age.data,
                        address = form.address.data,
                        city = form.city.data,
                        state = form.state.data,
                        zip_code = form.zip_code.data,
                        
                        climbing_gym = form.climbing_gym.data,
                        climbing_preference = form.climbing_preference.data,
                        
                        email = form.email.data,
                        password = form.password.data, 
                        role_id = 2)
            db.session.add(user)
            db.session.commit()
            token = user.generate_confirmation_token()
            send_email(user.email, 'Confirm Your Account',
                       'auth/email/confirm', user = user, token = token)
            flash(f"Alright, {form.first_name.data}, a confirmation email has been sent!")
        except SQLAlchemyError as e:
            print(str(e))
            flash('An error occurred.')
            db.session.rollback
            print(request.form)
        finally:
            db.session.close()
        return redirect(url_for('main.index'))
    return render_template('auth/signup.html', form = form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash("Invalid email and/or password. Please try again. ")
    return render_template('auth/login.html', form = form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))


@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.blueprint != 'auth' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))
    

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account',
               'auth/email/confirm', user = current_user, token = token)
    flash('A new confirmation email has just been sent!')
    return redirect(url_for('main.index'))