VENV_DIR := venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip

# Search for .env File
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

# Check if the virtual environment exists; if not, create it
$(VENV_DIR)/bin/activate: requirements.txt
	@test -d $(VENV_DIR) || ( \
		echo "Creating virtual environment..."; \
		python3 -m venv $(VENV_DIR); \
		$(PIP) install --upgrade pip; \
		$(PIP) install -r requirements.txt \
	)

# Install dependencies inside the virtual environment
install-dependencies: $(VENV_DIR)/bin/activate
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

# Start the Flask application
start-flask: install-dependencies
	$(PYTHON) -m flask run

# Resume the Flask application without additional setup (restart server)
resume-flask:
	$(PYTHON) -m flask run

# Run tests using pytest, ensuring the test database exists
test-flask: install-dependencies
	$(PYTHON) -m pytest

# Linting target
lint-flask: $(VENV_DIR)/bin/activate
	@echo "Running pylint on app and tests directories..."
	pylint app tests || { echo "Linting failed"; exit 1; }


# Docker build the application
docker-build:
	@echo "Building Docker image"
	docker build -t $(DOCKER_IMAGE):$(TAG) .

#  Run Flask-api using the docker compose
run-flask: docker-build
	docker-compose up -d  flask-api 

# Tagging
docker-tag:
	@echo "Tagging Docker image"
	docker tag $(DOCKER_IMAGE):$(TAG) $(DOCKER_USER)/$(DOCKER_IMAGE):$(TAG)

# Target to docker login
docker-login:
	docker login -u $(DOCKER_USERNAME) -p $(DOCKER_PASSWORD)


# Docker push the built image
docker-push: docker-build docker-tag
	@echo "Pushing Docker image to DockerHub"
	docker login -u $(DOCKER_USERNAME) -p $(DOCKER_PASSWORD)
	@echo "Pushing Docker image to Docker Hub..."
	docker push $(DOCKER_USER)/$(DOCKER_IMAGE):$(TAG)

# Run the complete pipeline (build, tag, and push)
all: docker-push


# Cleanup: remove virtual environment and other generated files (but not migrations)
clean:
	rm -rf $(VENV_DIR)
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	

# Full cleanup, including Alembic migrations (use with caution)
clean-full: clean
	rm -rvf .mypy_cache .pytest_cache/