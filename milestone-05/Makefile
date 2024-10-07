# Build the containers
build:
	docker-compose build

# Start the containers in detached mode
up:
	docker-compose up -d

# Stop the containers
down:
	docker-compose down

# Clean up (remove volumes and networks)
clean:
	docker-compose down --volumes --remove-orphans

# Deploy the application
deploy: build up