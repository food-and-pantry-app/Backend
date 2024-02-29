<p align="center">
  <img src="pics/pals.png" alt="Pantry Pals">
</p>

# DineIn Backend Setup Guide

Welcome to the DineIn backend setup guide! This document will walk you through the steps to get the backend part of the DineIn application up and running on your local machine. Our backend is built using Python/Flask and MongoDB, providing API services for the DineIn app.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- Python 3.7 or newer
- pip (Python package installer)
- MongoDB
- Homebrew (for macOS users)

## Getting Started

1. **Clone the Repository**

   First, clone the backend repository to your local machine:

   ```
   git clone https://github.com/food-and-pantry-app/Backend
   cd backend
   ```
2. **Setup Virtual Environment**

   It's a good practice to use a virtual environment for Python projects. This keeps your project's dependencies isolated from your global Python environment.

   ```
   python -m venv venv
   ```

   Activate the virtual environment:

   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```
3. **Install Dependencies**

   With the virtual environment activated, install the project dependencies:

   ```
   pip install -r requirements.txt
   ```
4. **Start MongoDB**

   Ensure MongoDB is installed and set up on your system. You can start MongoDB using Homebrew with the following command:

   ```
   brew services start mongodb/brew/mongodb-community
   ```
5. **Start the Flask Application**

   Use the provided `startProject.sh` script to start the Flask application along with MongoDB. This script activates the virtual environment, starts MongoDB, and runs the Flask app:

   ```
   chmod +x startProject.sh
   ./startProject.sh
   ```

   This will start the Flask development server, making the backend accessible at `http://127.0.0.1:5000`.

## What's Next?

After setting up the backend, you can begin developing features, connecting with the database, and testing endpoints using tools like Postman or curl.

## Additional Notes

- **MongoDB Setup**: If you encounter issues starting MongoDB, please refer to the [official MongoDB documentation](https://docs.mongodb.com/manual/installation/) for detailed setup instructions.
- **Virtual Environment**: Always activate the virtual environment (`source venv/bin/activate` or `venv\Scripts\activate`) before working on the project to ensure you're using the correct Python and dependencies.
- **Troubleshooting**: For any setup issues or if commands fail, double-check you have the correct versions of Python and pip installed, and that MongoDB is properly set up and running.
