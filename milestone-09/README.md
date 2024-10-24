**1. Project Title**

Setup one-click deployments using ArgoCD

**2. Project Description**

The project involves setup the REST API in kubernetes cluster using the helm and ArgoCD.


**3. Requirements**

- minikube
- kubectl
- docker
- helm
- vault
- argocd
- external-secrets
- postman
- vscode

**4. Setup the kubernetes cluster**

- Kubernetes config File information

```bash
# Kubectl path
/home/<home_user>/.kube

# kubectl configuration file
File: config

# Command to check the config file
$kubectl config view
```

- Minikube setup

```bash
# Download the latest minukube
$curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb

# Install the minukube
$sudo dpkg -i minikube_latest_amd64.deb

# Check the minukube status
$minikube status

# Start the minikube
$minikube start

# Check minikube on browser
$minikube dashboard
```

- Create Cluster with 4 nodes

```bash
# Check the minikube profile
$minikube profile list 

# Start with minikube profile
$minikube start --nodes 4 -p cluster

# custom resource 
$minikube start --cpus=2 --memory=4096 --nodes 4 -p cluster

# metric server
$minikube addons enable metrics-server --profile=cluster
 
# make profile active: 

$minikube profile list

$minikube profile cluster
- minikube profile was successfully set to cluster

# Set Labels

$kubectl label nodes cluster-m02 type=application
$kubectl label nodes cluster-m03 type=dependent_services
$kubectl label nodes cluster-m04 type=observability

#check lables

$kubectl get nodes --show-labels

# Create the taint for respective labels (node.yaml)**
Create the node.yaml file

# Generate the label for clusters
kubectl apply -f node.yaml

# Describe nodes info with labels
kubectl describe node cluster-m02

```

- Create the namespace

```bash
# create the namespace.yaml file for create the namespace.

# Apply the manifest

$kubectl apply -f namespaces.yaml

# Get the manifest output.
kubectl get namespaces

```
**5. Setup the ArgoCD** 

Step1: Add argocd repo

```bash
helm repo add argo https://argoproj.github.io/argo-helm
```

Step2: Install the argocd using the argocd namespace.


List of argocd pods.

```bash
argocd-application-controller-0
argocd-applicationset-controller-858cddf5cb-dkx6t
argocd-dex-server-f7794994f-4vn8k
argocd-notifications-controller-d988b477c-b5fql
argocd-redis-5bd4bbb-mslfh
argocd-repo-server-6d9f6bd866-kpw6q
argocd-server-59bb5df9fd-l6stq

```

step4: install argocd using the values.yaml (values refer to node afinity)

```bash
helm install argocd argo/argo-cd --namespace argocd --create-namespace -f values.yaml
```

Step5: Retrive the password for argocd
```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

Step6: Access the argocd dashboard
```bash
kubectl port-forward service/argocd-server -n argocd 8080:443 &
```

Step7: Create the argocd manifest the file is( argocd-app.yaml.) & apply it for Argocd application.

```bash
# apply the argocd manifest.
$kubectl apply -f  argocd/argocd-app.yaml 
```

Step8: make changes in CI pipeline
```bash
- pipeline must me run in main branch.
- env variable make changes in tag.
- add name in name section to update images tag in values.yaml.

```

Step9: update the same in main branch and it automatic update the docker image tag changes

```bash
git add .
git commit -m "update the CI pipeline for tag changes"
git push origin main

```

Step10: Check the image tag name in docker hub repository.


- Check the value.yaml file : the same image tag is same as docker hub image tag name.

```bash
api:
  replicaCount: 1

  image:
    repository: rajeshecb70/flask-api
    tag: "9.1.1"

  migrationImage:
    repository: rajeshecb70/flask-api
    tag: "9.1.1"
```

- Go to argo CD dashboard to check health status and commit message & images tag number.



Step11: To verify the commit message 

- check the commit message in pipeline.
- The commit head  as below is same as argocd dashboard message. 
```bash
To [https://github.com/***/one2n-sre-bootcamp](https://github.com/***/one2n-sre-bootcamp)

6de744f..6e28b3f  main -> main
```


**6. Check the api endpoints on postman**
```bash
#Healtch check
http://127.0.0.1:5000/healthcheck

# Check all points.
http://127.0.0.1:5000/api/v1/students

```

**7. delete the minikube**
```bash
minikube delete 
```
