## 1. Project Title
  Containerise REST API

## 2. Project Description

  - The project involves creating a basic CRUD API with Python and Flask & runs on Docker container
  - The API allows following operations on a student database:
    - Manage student records.
    - Add, retrieving, update, and delete students.
  - The project adheres to best practices in API development, including versioning, proper use of HTTP verbs, database migrations, and meaningful logging.

## 3. Requirements
    - Python 3.12.3
    - Flask 3.0.3
    - MySQL 8.0
    - pytest 8.3.3
    - Docker 24.0.7

## 4. Setup
   
   ```
   # Clone the repository
   git clone git@github.com:rajeshecb70/one2n-sre-bootcamp.git
   cd one2n-sre-bootcamp/milestone-02
   ```
   ```
   # Set up environment variables. Database mysql msut be install the below details required:
   DATABASE_HOST = <local Server IP>
   DATABASE_PORT = 3306
   DATABASE_USERNAME = <Your Database User>
   DATABASE_PASSWORD = <Your Database password>
   
   ```
   ```
   # Create a virtual environment, activate & build the application:
   make build
   ```
```
# Run the application:
make run
``` 
```
## 5. API Endpoints

- **POST /api/v1/students** - Add a new student.
- **GET /api/v1/students** - Get all students.
- **GET /api/v1/students/<id>** - Get a student by ID.
- **PUT /api/v1/students/<id>** - Update a student by ID.
- **DELETE /api/v1/students/<id>** - Delete a student by ID.
- **GET /healthcheck** - Health check endpoint.
  
## 6. Postman Collection

## 7.Expectations
- The following expectations should be met to complete this milestone.
  - API should be run using the docker image.✅

  - Dockerfile should have different stages to build and run the API.✅
    - Its reduce the docker image size.

  - We should be able to inject environment variables while running the docker container at runtime.✅

  - README.md should be updated with proper instructions to build the image and run the docker container.✅

  - Similarly appropriate make targets should be added in the Makefile.✅

  - The docker image should be properly tagged using semver tagging, use of latest tag is heavily discouraged.✅

  - Appropriate measures should be taken to reduce docker image size. We want our images to have a small size footprint.
   