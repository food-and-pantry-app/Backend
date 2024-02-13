<p align="center">
  <img src="pics/pals.png" alt="Pantry Pals">
</p>

# DineIn

Welcome to **PantryPalz**, a comprehensive solution designed to streamline your food and pantry management. This project leverages modern web technologies to provide a user-friendly interface for tracking pantry items, planning meals, and sharing recipes. This document provides detailed instructions to get you started with the project, along with an overview of the technologies being used.

## Technologies Used

- **Frontend**:

  - **React**: A JavaScript library for building user interfaces. [React Documentation](https://reactjs.org/docs/getting-started.html)
  - **Vite**: A build tool that aims to provide a faster and leaner development experience for modern web projects. [Vite Documentation](https://vitejs.dev/guide/)
- **Backend**:

  - **Python/Flask**: A lightweight WSGI web application framework. It's designed to make getting started quick and easy, with the ability to scale up to complex applications. [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
  - **MongoDB**: A source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. [MongoDB Documentation](https://docs.mongodb.com/)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Node.js and npm**: [Download Node.js and npm](https://nodejs.org/en/download/)
- **Python**: [Download Python](https://www.python.org/downloads/)
- **MongoDB**: [Install MongoDB](https://docs.mongodb.com/manual/installation/)

### Initial Setup

1. **Clone the Repository**:
   First, navigate to the directory where you want to clone the repository:

   Then, clone the repository and navigate into it:

   ```
   git clone https://github.com/food-and-pantry-app/pantrypalz.git
   cd pantrypalz
   ```
2. **Frontend Setup**:
   Install dependencies and start the frontend development server:

   ```
   cd frontend
   npm install
   npm run dev
   ```

   Your frontend should now be running and accessible.
3. **Backend Setup**:
   Set up the backend environment, install dependencies, and start the Flask application:

   ```
   cd ../backend
   python -m venv venv
   source venv/bin/activate  # Unix/macOS
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   flask run
   ```

   Your backend API should now be up and running.
4. **Database Configuration**:
   Make sure MongoDB is running on your system. Follow the MongoDB setup instructions specific to your operating system in the MongoDB documentation linked above.

## Development Practices

- **Coding Standards**: Adhere to the [PEP 8](https://pep8.org/) style guide for Python and the [Airbnb JavaScript Style Guide](https://airbnb.io/javascript/) for JavaScript.
- **Commit Messages**: Write clear, meaningful commit messages that accurately describe your changes.
- **Pull Requests**: All changes should be submitted via pull requests and reviewed by at least one other team member before merging.

## Additional Resources

- **React**: To get more familiar with React, check out the [official React tutorial](https://reactjs.org/tutorial/tutorial.html).
- **Flask**: For Flask, the [Flask Mega-Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) is an excellent comprehensive resource.
- **MongoDB**: Enhance your MongoDB skills through courses available at [MongoDB University](https://university.mongodb.com/).

## Getting Help

If you encounter any problems or have questions, please file an issue on the GitHub repository, or reach out to the project maintainers directly.
