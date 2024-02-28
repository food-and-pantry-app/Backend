<p align="center">
  <img src="pics/pals.png" alt="Pantry Pals">
</p>

# DineIn

## Technologies Used

- **Frontend**: React with Vite for a fast development experience.
- **Backend**: Python/Flask for the server-side logic.
- **Database**: MongoDB, a NoSQL database, for storing user data and recipes.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Node.js and npm: [Node.js download](https://nodejs.org/en/download/)
- Python: [Python download](https://www.python.org/downloads/)
- MongoDB: Follow the installation guide below.

### Installing MongoDB

1. **Install MongoDB**: Visit the [official MongoDB installation guide](https://docs.mongodb.com/manual/installation/) and follow the instructions for your operating system.
2. **Start MongoDB**: Once installed, you can start MongoDB on your system. The command may vary depending on your operating system. For most systems, the command is as follows:

   ```
   brew services start mongodb/brew/mongodb-community
   ```

   This command uses Homebrew for macOS. Adjust accordingly for your OS.

### Setting Up the Project

1. **Clone the Repository**:
   Open your terminal, navigate to the directory where you want to clone the repository, and run:

   ```
   git clone https://github.com/food-and-pantry-app/dinein.git
   cd dinein
   ```
2. **Frontend Setup**:
   Navigate to the frontend directory, install dependencies, and start the development server:

   ```
   cd frontend
   npm install
   npm run dev
   ```
3. **Backend Setup**:
   Set up the Python virtual environment, activate it, install dependencies, and start the Flask application:

   ```
   cd ../backend
   python -m venv venv
   source venv/bin/activate  # Unix/macOS
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ./startProject.sh
   ```

### Testing Endpoints with curl

After setting up both the frontend and backend, you can test the API endpoints. Here are some sample curl commands:

- **Create a New User**:
  ```
  curl -X POST http://127.0.0.1:5000/api/v1/users/ -H "Content-Type: application/json" -d '{...your JSON data here...}'
  ```
- **Retrieve a User by UserID**:
  ```
  curl http://127.0.0.1:5000/api/v1/users/<UserID>
  ```

  Replace `<UserID>` with the actual user ID from your MongoDB.

## Development Practices

- Follow the [PEP 8 style guide](https://pep8.org/) for Python and the [Airbnb JavaScript Style Guide](https://airbnb.io/javascript/) for JavaScript.
- Write clear, meaningful commit messages.
- Submit changes via pull requests and ensure at least one team member reviews them before merging.

## Additional Resources

- React Tutorial: [official React tutorial](https://reactjs.org/tutorial/tutorial.html)
- Flask Tutorial: [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- MongoDB University: [MongoDB courses](https://university.mongodb.com/)d
