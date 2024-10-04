# Search for .env File
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
DOCKER_USER?=rajeshecb70
DOCKER_IMAGE?=flask-api
TAG?=3.0.1


# Check if the virtual environment exists; if not, create it........
$(VENV_DIR)/bin/activate: requirements.txt
	@test -d $(VENV_DIR) || ( \
		echo "Creating virtual environment..."; \
		python3 -m venv $(VENV_DIR); \
		$(PIP) install --upgrade pip; \
		$(PIP) install -r requirements.txt \
	)

#  Run database using the docker compose.
run-db:
	docker-compose up -d db && sleep 10

# Install dependencies inside the virtual environment....
install-dependencies: $(VENV_DIR)/bin/activate
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

#Target to initiate the migration.
init-migration:
	$(PYTHON) -m flask db init

# Target to generate the migration. (The message must comply with the app's requirements)..
generate-migration:
	$(PYTHON) -m flask db migrate -m "(Automatic generate the migration)"

# Run tests using pytest, ensuring the test database exists
test-flask:
	# Pass DATABASE_URL as an environment variable.
	# DATABASE_URL=$(DATABASE_URL) $(PYTHON) -m pytest
	pytest app tests

# Linting target...
lint-flask: $(VENV_DIR)/bin/activate
	@echo "Running flake8 on app and tests directories..."
#flake8 app tests && echo "No linting errors found!" || { echo "Linting failed with error code $$?"; exit 1; }
	flake8 app tests

# Docker build the application
docker-build:
	@echo "Building Docker image"
	docker build -t $(DOCKER_IMAGE):$(TAG) . 

# Tagging
docker-tag:
	@echo "Tagging Docker image"
	docker tag $(DOCKER_IMAGE):$(TAG) $(DOCKER_USER)/$(DOCKER_IMAGE):$(TAG)

# Target to docker login.
docker-login:
	docker login -u $(DOCKER_USERNAME) -p $(DOCKER_PASSWORD)

# Docker push the built image
docker-push: docker-build docker-tag
	@echo "Pushing Docker image to DockerHub"
	docker login -u $(DOCKER_USERNAME) -p $(DOCKER_PASSWORD)
	@echo "Pushing Docker image to Docker Hub..."
	docker push $(DOCKER_USER)/$(DOCKER_IMAGE):$(TAG)

#  Run Flask-api using the docker compose..
run-flask:
	docker-compose --env-file api.env up -d

# Run the complete pipeline (build, tag, and push)
all:run-db install-dependencies init-migration generate-migration test-flask  docker-push run-flask

# Target to stop container 
stop:
	docker-compose down

# Cleanup: remove virtual environment and other generated files (but not migrations)
clean:
	rm -rf $(VENV_DIR)
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

# Full cleanup, including Alembic migrations (use with caution)
clean-full: clean
	rm -rvf .mypy_cache .pytest_cache/