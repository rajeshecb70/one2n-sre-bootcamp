## 1. Project Title
  Milestone-03: Setup one-click local development setup

## 2. Project Description
  This project runs a Flask API using Docker, leveraging multi-stage builds to minimize the image size. The API interacts with a MySQL database and supports migrations.


## 3. Prerequisites
  - Docker and Docker Compose installed.
  - MySQL running in a container.
  - .env file for database details. (DATABASE_URL=mysql+pymysql://root:<DBpassword>@localhost/databasename)


## 4. Setup & configuration of milestone-03
  ```
  # Clone the repository
  git clone https://github.com/rajeshecb70/one2n-sre-bootcamp.git
  cd one2n-sre-bootcamp/milestone-03
  ```
    ```
  # Target to intiate the migration.
  make init-migration
  ```
  ```
  # Target to generate the migration.
  make generate-migration
  ```

  ```
  # Target to start the DB container
  make run-db
  ```
  ```
  # Target to run application and db with migration.
  make all
  ```
  ```
  # Target to build REST API docker image
  make build-flask
  ```

  ```
  # Target to start the database container
  make run-flask
  ```

  ```
  # Target to stop flask API container
  make stop-flask
  ```
  ```
  # Target to stop flask Database container
  make stop-db
  ```

  ```
  # Target to stop all services
  make stop
  ```

  ```
  # Target to clean the temporary files.
  make full_clean
  ```

### 5. Expectations
  - The following expectations should be met to complete this milestone.
    - API and its dependent services should be run using docker-compose.✅
    - Makefile should have the following targets.
      - To start DB container.✅
      - To run DB DML migrations.✅
      - To build REST API docker image.✅
      - To run REST API docker container.✅

    - README.md file should be updated with instructions
      - To add pre-requisites for any existing tools that must already be installed (e.g., docker, make, etc)✅
      - To run different make targets and the order of execution.✅

    - When we run the make target to start the REST API docker container.
      - It should first start the DB and run DB DML migrations.✅
      - (Good to have) You can even include checks to see if the DB is already running and DB migrations are already applied.
      - Later it should invoke the docker compose command to start the API docker container.