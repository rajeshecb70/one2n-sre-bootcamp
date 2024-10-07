## 1. Project Title

Milestone-04 : Setup a CI pipeline with github actions

## 2. Project Description

This project aims to set up a Continuous Integration (CI) pipeline using GitHub Actions. The pipeline is designed to automate the process of building, testing, linting, and deploying a Dockerized application. By implementing this pipeline, developers can ensure code quality and streamline the deployment process to a central Docker registry, such as DockerHub or GitHub Docker registry.

## 3. Prerequisites

- Docker and Docker Compose.
- Make
- Github actions login details fir run the CI and manage the secrets.
- Self hosted runner
- dockerhub login details.
- Milestone-04-CI.yml is stored at .github/workflow/milestone-04-CI.yml
- You should Have self-hosted runner configured on you github repository.
- Configure secrets on github repos with DATABASE_RUL, DOCKER_USERNAME & DOCKER_PASSWORD

## 4. Setup & configuration of milestone-04

```
# Clone the repository
git clone https://github.com/rajeshecb70/one2n-sre-bootcamp.git
cd one2n-sre-bootcamp/milestone-04
```

```
# Check the status of pipeline

After making changes to the code and pushing them to your repository, the pipeline will automatically trigger. You can monitor the status and progress of the pipeline by navigating to GitHub Repository > Actions > All Workflows.
```

We have created a CI pipeline using GitHub Actions. This pipeline is triggered automatically whenever code is pushed to the repository or changes are made in the working directory.

### 5. Expectations

The following expectations should be met to complete this milestone.
CI pipeline should consist of the following stages

- Build API
- Run tests
- Perform code linting
- Docker login
- Docker build and push

- To achieve the stages of building, testing, and performing code linting, you need to use appropriate make targets.✅
- CI pipeline should be run using a self-hosted GitHub runner running on your local machine.✅
- CI pipeline should only be triggered when changes are made in the code directory and not in other directories or filepaths.✅
- CI workflow should allow the developer to manually trigger the pipeline when required.✅
