## 1. Project Title
  Create a simple REST API Webserver:  Student API

## 2. Project Description

  - The project involves creating a basic CRUD API with Python and Flask. 
  - The API allows following operations on a student database:
    - Manage student records.
    - Add, retrieving, update, and delete students.
  - The project adheres to best practices in API development, including versioning, proper use of HTTP verbs, database migrations, and meaningful logging.

## 3. Requirements
    - Python 3.12.3
    - MySQL 8.0

## 4. Setup
  ```
  git clone git@github.com:rajeshecb70/one2n-sre-bootcamp.git
  cd one2n-sre-bootcamp/milestone-01
  ```

  ```
  # Create a virtual environment, activate & run it:
  make all
  ```
  ```
  # Set up environment variables. Create a `.env` file and add:
  DATABASE_URL=mysql+pymysql://user:paassword@localhost/studentdb
  ```

```
# Run the application:
make run
```
```
# Run migrations to set up the database:
make migrate
``` 
```
# To run tests:
make test
```

## API Endpoints

- **POST /api/v1/students** - Add a new student.
- **GET /api/v1/students** - Get all students.
- **GET /api/v1/students/<id>** - Get a student by ID.
- **PUT /api/v1/students/<id>** - Update a student by ID.
- **DELETE /api/v1/students/<id>** - Delete a student by ID.
- **GET /healthcheck** - Health check endpoint.
  

## 6. Postman Collection