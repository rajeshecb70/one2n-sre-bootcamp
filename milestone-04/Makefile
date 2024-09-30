# Search for .env File
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

# Step 1: Build the API using docker-compose or Dockerfile
build:
	docker-compose build flask-api --no-cache

# Step 2: Run tests using pytest (assuming your tests use pytest)
run: build
	docker-compose up -d  flask-api 
test:
	docker-compose run pytest tests/

# Step 3: Perform linting using flake8 or any linting tool you use (flake8 in this example)
lint:
	docker-compose run --rm flask-api flake8 .

# Step 5: Docker build the application
docker-build:
	@echo "Building Docker image"
	docker build -t $(DOCKER_IMAGE):$(TAG) .

# Tagging
docker-tag:
	@echo "Tagging Docker image"
	docker tag $(DOCKER_IMAGE):$(TAG) $(DOCKER_USER)/$(DOCKER_IMAGE):$(TAG)


# Step 6: Docker push the built image
docker-push: docker-build docker-tag
	@echo "Pushing Docker image to DockerHub"
	docker login -u $(DOCKER_USERNAME) -p $(DOCKER_PASSWORD)
	@echo "Pushing Docker image to Docker Hub..."
	docker push $(DOCKER_USER)/$(DOCKER_IMAGE):$(TAG)

# Run the complete pipeline (build, tag, and push)
all: docker-push