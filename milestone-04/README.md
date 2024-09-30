## 1. Project Title
  Milestone-04 : Setup a CI pipeline

## 2. Project Description
  This project runs a Flask API using Docker, leveraging multi-stage builds to minimize the image size. The API interacts with a MySQL database and supports migrations using github Actions.


## 3. Prerequisites
  - Docker and Docker Compose installed.
  - MySQL running in a container.
  - .env file for database details. (DATABASE_URL=mysql+pymysql://root:<DBpassword>@localhost/databasename)
  - Github actions required.


## 4. Setup & configuration of milestone-03
  ```
  # Clone the repository
  git clone https://github.com/rajeshecb70/one2n-sre-bootcamp.git
  cd one2n-sre-bootcamp/milestone-04
  ```
  ```
  # Target for Build API image
  make docker-build
  ```

  ```
  # Target to Run tests
  make test-flask
  ```

  ```
  # Target to Perform code linting
  make lint-flask
  ```

  ```
  # Target to Docker login
  make docker-login
  ```

  ```
  # Target to Docker build and push
  make all
  ```
  ```
  # Target to stop flask Database container
  make stop-db
  ```

  ```
  # Target to clean some files.
  make clean
  ```

  ```
  # Target to clean-full the temporary files.
  make clean-full
  ```

### 5. Expectations
The following expectations should be met to complete this milestone.

    CI pipeline should consist of the following stages
        Build API
        Run tests
        Perform code linting
        Docker login
        Docker build and push

    To achieve the stages of building, testing, and performing code linting, you need to use appropriate make targets.

    CI pipeline should be run using a self-hosted GitHub runner running on your local machine.

    CI pipeline should only be triggered when changes are made in the code directory and not in other directories or filepaths.

    CI workflow should allow the developer to manually trigger the pipeline when required.