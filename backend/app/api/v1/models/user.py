from flask_pymongo import ObjectId
from app import mongo

class UserModel:
    @staticmethod
    def create_user(data):
        return mongo.db.users.insert_one(data).inserted_id

    @staticmethod
    def find_user_by_id(user_id):
        return mongo.db.users.find_one({"_id": ObjectId(user_id)})
