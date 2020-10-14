# from Climbr import app
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from . import main
# from .forms import UserForm
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    # form = UserForm
    # if form.validate_on_submit()
    #     #
    #     return redirect(url_for('.index'))

    return render_template('home.html')

