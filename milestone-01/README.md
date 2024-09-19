# Python Flask Application

This project is a Flask web application that can be run locally using Docker and Flask. The application also supports database migrations and running tests with `pytest`.

## Requirements

- Python 3.12.3
- Flask 3.0.2
- pytest 7.4.4
- MySql 8.0

## Local Setup Instructions

### 1. Install Dependencies

Make sure all required dependencies are installed using `pip`:
```bash
pip install -r requirements.txt

### 2. Running the Application Locally
```bash
make run

- This will:

   --  Set FLASK_APP=app and FLASK_ENV=development
   --  Start the Flask application on port 5001

- Once the app is running, you can access it in your browser at:

   --  Healthcheck: http://localhost:5001/healthcheck
   --  Students API: http://localhost:5001/api/v1/students

### 3. Database Migrations
- The project includes support for database migrations using Flask-Migrate. You can manage migrations with the following commands:
Migrate the Database:

- To generate and apply new migrations:

```bash
make migrate

-This will:

   --  Run flask db migrate with the message "Initial migration."
   --  Apply the migrations using flask db upgrade

### 4. Running Tests

- Tests are written using pytest. To run the tests:

```bash
make test

- This will:

   --  Set the PYTHONPATH and run pytest to execute the test suite.

## 5. Code Linting

- If you have flake8 installed for code linting, you can uncomment the lint section in the Makefile and use:

```bash
make lint

- This will run flake8 on your code to check for linting issues.
