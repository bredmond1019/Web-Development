from Climbr import app
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify


@app.route('/')
def index():
    return render_template('home.html')