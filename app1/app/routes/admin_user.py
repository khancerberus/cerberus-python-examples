# type: ignore
from flask import jsonify
from flask import request

from app.models import User
from app.models.user import validate_user

from . import app_bp


@app_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()

    return jsonify({
        'message': 'success',
        'users': [user.json() for user in users]
    }), 200


@app_bp.route('/users', methods=['POST'])
def create_user():
    results = validate_user(request.get_json())

    if results.errors:
        return jsonify(
            message='error validating user data',
            errors=results.errors
        ), 400

    new_user = User(
        name=results.document['name'],
        age=results.document['age']
    )
    new_user.save()

    return jsonify(
        message='success',
        user=new_user.json()
    ), 201


@app_bp.route('/users/<int:user_id>', methods=['POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(message='user not found'), 404

    results = validate_user(request.get_json(), update=True)

    if results.errors:
        return jsonify(
            message='error validating user data',
            errors=results.errors
        ), 400

    if 'name' in results.document:
        user.name = results.document['name']

    if 'age' in results.document:
        user.age = results.document['age']

    user.save()

    return jsonify(
        message='success',
        user=user.json()
    ), 200
