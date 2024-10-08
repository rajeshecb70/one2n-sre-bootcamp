#!/bin/bash

# Function to install Docker
install_docker() {
    echo "Installing Docker..."
    sudo apt-get update
    sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install -y docker-ce
    sudo usermod -aG docker vagrant
}

# Function to install Docker Compose
install_docker_compose() {
    echo "Installing Docker Compose..."
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
}

# Function to install Make
install_make() {
    echo "Installing Make..."
    sudo apt-get install -y build-essential
}

# Function to start the deployment
start_deployment() {
    echo "Starting the deployment..."
    cd /vagrant
    make deploy
}

# Function to start the database
start_deploymentdb() {
    echo "Starting the deployment..."
    cd /vagrant
    make deploy-db
}

# Execute functions
install_docker
install_docker_compose
install_make
start_deploymentdb
start_deployment
