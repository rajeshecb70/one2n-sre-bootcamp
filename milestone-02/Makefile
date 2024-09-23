# Makefile

# Variables
IMAGE_NAME = my-flask-api
CONTAINER_NAME = my-flask-api-container
DOCKERFILE_PATH = Dockerfile
TAG = 1

# Default target when running "make"
.PHONY: all
all: build

# Build the Docker image
.PHONY: build
build:
	docker build -t $(IMAGE_NAME):$(TAG) -f $(DOCKERFILE_PATH) .

# Run the Docker container
.PHONY: run
run:
#	# docker run -p 5000:5000 --network host -e DB_HOST=172.17.0.1 -e DB_USER=rajesh -e DB_PASSWORD=One2n_One2n $(IMAGE_NAME):$(TAG)
	docker run -d --network host $(IMAGE_NAME):$(TAG)

# List Docker images
.PHONY: images
images:
	docker images

# Stop and remove the Docker container
.PHONY: stop
stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

# Clean up images
.PHONY: clean
clean:
	docker rmi $(IMAGE_NAME):$(TAG)
