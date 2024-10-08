## 1. Project Title

Milestone-05 : Deploy REST API & its dependent services on bare metal

## 2. Project Description

This project aims to set up REST API container using the vagrant. We have spin up the 1 nginx. 2 APIs and 1 DB containers.

## 3. Prerequisites

- Vagrant
- Docker and Docker Compose.
- Make
- Virtualbox

## 4. Setup & configuration of milestone-04

```
# Clone the repository
git clone https://github.com/rajeshecb70/one2n-sre-bootcamp.git
cd one2n-sre-bootcamp/milestone-05
```

```
# Intialize the vagrant
vagrant init
```

```
# Start the vagrant
vagrant up
```

```
# Provision the vagrant
vagrant provision
```

### 5. Expectations

The following expectations should be met to complete this milestone.

- Vagrant box should be spun up using Vagrantfile.✅
- For setting up the Vagrant box you need to use the bash script with functions to install the required dependencies.✅
- You need to use the docker-compose and Makefile to do the deployment.✅
- The final setup should consist of: 2 API containers, 1 DB container, 1 Nginx container ✅
- The Nginx deployment configuration should be committed in the GitHub repository along with the Nginx config.✅
- Nginx should be used for load balancing between these two API containers.✅
- API should be accessible via port 8080 and internally should load balance requests between two API containers.✅
- You should get status code 200 while making the request using Postman collection for different API endpoints.✅
