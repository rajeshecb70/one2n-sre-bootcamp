# Search for .env File
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

# Define version as a variable for easy updating
IMAGE_NAME = flask-api
DOCKERFILE_PATH = Dockerfile
TAG = 3.1.0

# Target to initailize the migration 
init_migration:
	flask db init 

# Target to generate the migration. (The message must comply with the app's requirements)
generate_migration:
	flask db migrate -m "(The message must comply with the app's requirements)"

# Target to start the DB container
run-db:
	docker-compose up -d db

# Target to start the application container and run migration
all: build run

# Target to build flask image with tag
build-flask:
	docker build -t $(IMAGE_NAME):$(TAG) .

# Target to run flask container.
run-flask:
	docker-compose up -d flask-api

# Target to stop flask container.
stop-flask:
	docker-compose down flask-api

# Target to stop Database container.
stop-db:
	docker-compose down db

# Target to stop all container
make stop:
	docker-compose down

# Target to clean container and images.
#clean:
#	docker-compose down -v
#	docker system prune -f
#	docker volume prune -f

# Target to clean the temporary files.
full-clean:
	rm -rvf .mypy_cache
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

	