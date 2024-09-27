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

	