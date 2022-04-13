from flask import render_template, Response, jsonify, request
from . import api
from ..models import Wombat
from backend import db
from datetime import datetime


@api.route('/')
def index():
    return Response("Inspire Candidate Exercise", content_type='text/plain')


@api.route("/wombats", methods=['GET'])
def get_wombats():
    wombats = Wombat.query.all()

    data = [wombat.to_dict() for wombat in wombats]

    return jsonify({"wombats": data}), {'Content-Type': 'application/json'}


@api.route("/wombats", methods=['POST'])
def post_wombats():
    data = request.form

    if "name" not in data:
        return "Missing parameter: name", 400
    if "dob" not in data:
        return "Missing parameter: dob", 400

    dto = datetime.strptime(data["dob"], '%Y-%m-%d').date()

    new_wombat = Wombat(name=data["name"], dob=dto)
    db.session.add(new_wombat)
    db.session.commit()

    return jsonify(new_wombat.to_dict())
