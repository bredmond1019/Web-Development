from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from . import auth
from .forms import SignUpForm, LoginForm
from ..models import User




@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        try:
            print(request.form)
        except Exception as e:
            print(str(e))
        return redirect(url_for('.index'))
    return render_template('auth/signup.html')

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