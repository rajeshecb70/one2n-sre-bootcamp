## 1. Project Title
  Setup one-click local development setup

## 2. Project Description
  We want to simplify the process of setting up API on the local machine for development. The idea is to enable other team members to run the API and its dependent services with the least amount of steps involved in getting this up and running.

  We won’t be assuming that other team members have the required tools already installed on their local. So we will be going one step further and providing them with simple bash functions to install the required tools.


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
  cd one2n-sre-bootcamp/milestone-03
  ```
      
  ```
  # Target to start the DB container
start-db:
	docker-compose up -d db

# Target to run DB migrations.
run-migrations:
	docker-compose run flask-api flask db upgrade

# Target to build REST API docker image
build-api:
	docker-compose build flask-api

# Target to run REST API docker container
start-api: start-db run-migrations
	docker-compose up -d flask-api

# Target to stop all services
stop:
	docker-compose down
  ```