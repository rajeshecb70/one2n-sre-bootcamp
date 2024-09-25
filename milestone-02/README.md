## 1. Project Title
  Containerise REST API

## 2. Project Description
  The objective of this project is to develop a Dockerfile for a REST API that adheres to best practices for containerization. The resulting Docker image will facilitate easy deployment, ensure environment configurability, and maintain a small size footprint. This project emphasizes using multi-stage builds, appropriate tagging conventions, and clear documentation for building and running the API.


## 3. Requirements
    - Python 3.12.3
    - Flask 3.0.3
    - MySQL 8.0
    - pytest 8.3.3
    - Docker 24.0.7

## 4. Setup & configuration
   ```
  # Configuration

    Before running the commands, ensure that you have the following environment variables set:

  - `IMAGE_NAME`: The name of the Docker image.
  - `TAG`: The version tag for the Docker image (following semantic versioning).
  - `DOCKERFILE_PATH`: The path to the Dockerfile (default is `Dockerfile`).
  - `CONTAINER_NAME`: The name of the Docker container.
  - `DB_USER`: MySQL username for database access.
  - `DB_PASSWORD`: MySQL password for the specified user.
  - `DB_NAME`: The name of the main database.
  - `TEST_DB_NAME`: The name of the test database.
  - `PYTHON`: The Python interpreter (default is `python`).
  ```
   
  ```
  # Clone the repository
  git clone https://github.com/rajeshecb70/one2n-sre-bootcamp.git
  cd one2n-sre-bootcamp/milestone-02
  ```
      
  ```
  # Build the Docker Image
  make build
  ```
  ```
  # Run the Docker Container
  make run
  ```
  ```
  # Stop and Remove the Docker Container
  make stop
  ```
  ```
  # Clean Up Docker Images
  make clean
  ```
  ```
  # Clean Up Temp file and pyc files
  make full_clean:
  ```

  ```
  # Check MySQL Installation
  make check_mysql
  ```
  ```
  # Reset Alembic Version Table
  make reset_alembic
  ```
  ```
  # Initialize Alembic for migration 
  make alembic_init
  ```
  ```
  # Generate Migrations
  make migrate
  ```
  ```
  # Run migrations to set up the database:
  make migrate
  ``` 
  ```
  # Upgrade migrations to set up the database:
  make upgrade

    - The schema after upgradation.

  mysql> desc student;
  +--------------+--------------+------+-----+---------+----------------+
  | Field        | Type         | Null | Key | Default | Extra          |
  +--------------+--------------+------+-----+---------+----------------+
  | id           | int          | NO   | PRI | NULL    | auto_increment |
  | name         | varchar(100) | NO   |     | NULL    |                |
  | age          | int          | NO   |     | NULL    |                |
  | phone_number | int          | NO   |     | NULL    |                |
  | gender       | varchar(100) | NO   |     | NULL    |                |
  | address      | varchar(100) | YES  |     | NULL    |                |
  +--------------+--------------+------+-----+---------+----------------+

  ```

  ```
  # Upgrade migrations to set up the database:
  make downgrade
    - The Schema after downgrade (same as main original schema)
  mysql> desc student;
  +--------------+--------------+------+-----+---------+----------------+
  | Field        | Type         | Null | Key | Default | Extra          |
  +--------------+--------------+------+-----+---------+----------------+
  | id           | int          | NO   | PRI | NULL    | auto_increment |
  | name         | varchar(100) | NO   |     | NULL    |                |
  | age          | int          | NO   |     | NULL    |                |
  | phone_number | int          | NO   |     | NULL    |                |
  | gender       | varchar(100) | NO   |     | NULL    |                |
  +--------------+--------------+------+-----+---------+----------------+
  5 rows in set (0.00 sec)
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
  


## 6. Expectations
  - The following expectations should be met to complete this milestone.

    - API should be run using the docker image.✅

    - Dockerfile should have different stages to build and run the API.✅

    - We should be able to inject environment variables while running the docker container at runtime.✅

    - README.md should be updated with proper instructions to build the image and run the docker container.✅

    - Similarly appropriate make targets should be added in the Makefile.✅

    - The docker image should be properly tagged using semver tagging, use of latest tag is heavily discouraged.✅

    - Appropriate measures should be taken to reduce docker image size. We want our images to have a small size footprint.✅
      - Docker Image Size : 133MB