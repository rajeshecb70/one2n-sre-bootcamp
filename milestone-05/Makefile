DOCKER_IMAGE?=flask-api
TAG?=3.0.0

# Default container names
CONTAINER_NAME_API1?=api1
CONTAINER_NAME_API2?=api2
CONTAINER_NAME_DB?=db
CONTAINER_NAME_NGINX?=nginx

# Build the containers
build:
	DOCKER_IMAGE=$(DOCKER_IMAGE) TAG=$(TAG) \
	CONTAINER_NAME_API1=$(CONTAINER_NAME_API1) \
	CONTAINER_NAME_API2=$(CONTAINER_NAME_API2) \
	CONTAINER_NAME_DB=$(CONTAINER_NAME_DB) \
	CONTAINER_NAME_NGINX=$(CONTAINER_NAME_NGINX) \
	docker-compose build

# Start the containers in detached mode
db-up:
	CONTAINER_NAME_DB=$(CONTAINER_NAME_DB) \
	docker-compose up -d db

up:
	DOCKER_IMAGE=$(DOCKER_IMAGE) TAG=$(TAG) \
	CONTAINER_NAME_API1=$(CONTAINER_NAME_API1) \
	CONTAINER_NAME_API2=$(CONTAINER_NAME_API2) \
	CONTAINER_NAME_NGINX=$(CONTAINER_NAME_NGINX) \
	docker-compose up -d nginx api1 api2

# Stop the containers
down:
	docker-compose down

# Clean up (remove volumes and networks)
clean:
	docker-compose down --volumes --remove-orphans

# Deploy the application
deploy: build db-up up
