from flask import Blueprint, request, jsonify
from app.api.v1.models.user import UserModel
from bson.json_util import dumps

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/', methods=['POST'])
def create_user():
    data = request.json
    user_id = UserModel.create_user(data)
    return jsonify({"success": True, "UserID": str(user_id)}), 201

@user_blueprint.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = UserModel.find_user_by_id(user_id)
    if user:
        return dumps(user), 200
    else:
        return jsonify({"error": "User not found"}), 404
