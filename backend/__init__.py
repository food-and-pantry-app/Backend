from flask import Flask

app = Flask(__name__)

# Importing views to ensure route handlers are registered
from .views import recipe_view
