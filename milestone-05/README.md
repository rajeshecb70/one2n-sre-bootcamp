## 1. Project Title

Milestone-05 : Deploy REST API & its dependent services on bare metal

## 2. Project Description

This project involves the deployment of a REST API and its associated services utilizing Vagrant, Docker-Compose, and a Makefile to establish a production-ready environment. The objective is to provision a Vagrant box, representing the production environment, where all services are containerized and managed using Docker-Compose for streamlined orchestration. A bash script will be leveraged to automate the installation of required dependencies inside the Vagrant box, ensuring consistency and repeatability in the setup process.
The final infrastructure will comprise two API containers, one database (DB) container, and one Nginx container, forming a scalable, multi-tier architecture capable of efficiently managing traffic distribution and service availability.

## 3. Prerequisites

- Vagrant
- VirtualBox
- Docker and Docker Compose.
- Make

## 4. Setup & configuration of milestone-04

```
# Clone the repository
git clone https://github.com/rajeshecb70/one2n-sre-bootcamp.git
cd one2n-sre-bootcamp/milestone-05
```

```
# Initializing the vagrant
 vagrant init
```

```
# Provision the container 
 vagrant up --provision
```

### 5. Expectations

The following expectations should be met to complete this milestone.

- Vagrant box should be spun up using Vagrantfile.✅
- For setting up the Vagrant box you need to use the bash script with functions to install the required dependencies.✅
- You need to use the docker-compose and Makefile to do the deployment.✅
- The final setup should consist of
  > 2 API containers
  > 1 DB container
  > 1 Nginx container

- The Nginx deployment configuration should be committed in the GitHub repository along with the Nginx config.✅
- Nginx should be used for load balancing between these two API containers.✅
- API should be accessible via port 8080 and internally should load balance requests between two API containers.✅
