#!/bin/bash

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Start MongoDB
echo "Starting MongoDB..."
brew services start mongodb/brew/mongodb-community

# Start your Flask application
echo "Starting Flask app..."
export FLASK_APP=app.py  # Make sure this matches your Flask application's entry file
export FLASK_ENV=development # Enables debug mode for development, including auto-reload
flask run
