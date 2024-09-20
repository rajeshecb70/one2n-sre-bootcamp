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
    - Flask 3.0.3
    - MySQL 8.0

## 4. Setup
   
   ```
   # Clone the repository
   git clone git@github.com:rajeshecb70/one2n-sre-bootcamp.git
   cd one2n-sre-bootcamp/milestone-01
   ```
   ```
   # Set up environment variables. Create a `.env` file and add:
   DATABASE_URL=mysql+pymysql://user:paassword@localhost/studentdb
   ```
   ```
   # Create a virtual environment, activate & run the application:
   make all
   ```
```
# Run migrations to set up the database:
make migrate
``` 
```
# To run tests:
make test
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
   -  The following expectations should be met to complete this milestone.
         Create a public repository on GitHub. ✅
      
   -  The repository should contain the following
         README.md file explaining the purpose of the repo, along with local setup instructions. ✅
         
         Explicitly maintaining dependencies in a file ex (pom.xml, build.gradle, go.mod, requirements.txt, etc).✅

         Makefile to build and run the REST API locally. ✅

         bility to run DB schema migrations to create the student table. ✅

         Config (such as database URL) should not be hard-coded in the code and should be passed through environment variables. ✅

         Postman collection for the APIs. ✅

   -  API expectations

         Support API versioning (e.g., api/v1/students).✅

         Using proper HTTP verbs for different operations.✅

         API should emit meaningful logs with appropriate log levels.

         API should have a /healthcheck endpoint.✅

         Unit tests for different endpoints.