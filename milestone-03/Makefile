# Search for .env File
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

# Variables
IMAGE_NAME = my-flask-api
CONTAINER_NAME = my-flask-api-container
DOCKERFILE_PATH = Dockerfile
TAG = 3.0.0

# make all build image and run the container.
# all: build run migrate upgrade

# Build the Docker image
build:
#	#@docker build -t $(IMAGE_NAME):$(TAG) -f $(DOCKERFILE_PATH) .
	docker-compose -f docker-compose.yml up --build -d 

down:
	docker-compose -f docker-compose.yml down
# Run the Docker container
#run:
#	#@docker run -d --network host  --env-file .env --name $(CONTAINER_NAME) -e $(DATABASE_URL) $(IMAGE_NAME):$(TAG)

# Stop and remove the Docker container
#stop:
#	@docker stop $(CONTAINER_NAME) || true
#	docker rm $(CONTAINER_NAME) || true

# Clean up images
#clean:
#	docker rmi $(IMAGE_NAME):$(TAG)

# Check if MySQL is installed and user is created, then create the databases if they don't exist
#check_mysql:
#	@command -v mysql >/dev/null 2>&1 || { echo >&2 "MySQL is not installed. Aborting."; exit 1; }

# Reset Alembic version table in MySQL (if it exists)
#reset_alembic:
#	@mysql -u $(DB_USER) -p$(DB_PASSWORD) -e "DROP TABLE IF EXISTS $(DB_NAME).alembic_version;"

# Initialize Alembic (if not already initialized)
alembic_init:
#	@test -f migrations/env.py || 
	flask db init

# Generate a new migration based on the models.py schema
migrate:
	flask db migrate -m "Add gender"

# Apply the database migrations (run 'upgrade')
upgrade:
	flask db upgrade

# Apply the database migrations (run 'downgrade')
downgrade:
	flask db downgrade

# Create MySQL test database if it doesn't exist
#create_test_db:
#	@mysql -u $(DB_USER) -p$(DB_PASSWORD) -e "CREATE DATABASE IF NOT EXISTS $(TEST_DB_NAME);"

# Run tests using pytest, ensuring the test database exists
#test: create_test_db
#	$(PYTHON) -m pytest
# Cleanup: remove virtual environment and other generated files (but not migrations)
full_clean:
	rm -rvf .mypy_cache
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	