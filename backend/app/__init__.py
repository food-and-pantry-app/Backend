from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)

from app.api.v1.controllers.userController import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/api/v1/users")
