**1. Project Title**

Deploy REST API & its dependent services in K8s

**2. Project Description**

The project involves setup the REST API in kubernetes cluster using the below points.

- Manage the secrets using vault.
- External secrets operator manage secrets for apis.
- application and db deploy in container.
- Migration manage by the init container.
- Test the application using the application end point.

**3. Requirements**

- minikube
- kubectl
- docker
- helm
- vault
- external-secrets
- postman
- vscode

**4. Setup the kubernetes cluster**

**Step1: Kubernetes config File**

```bash
# Kubectl path
/home/<home_user>/.kube

# kubectl configuration file
File: config

# Command to check the config file
$kubectl config view
```

**Step2: Minikube setup:**

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

**Step:3 Create Cluster with 4 nodes**

```bash
# Check the minikube profile
$minikube profile list 

# Start with minikube profile
$minikube start --nodes 2 -p mycluster

# custom resource 
$minikube start --cpus=2 --memory=4096 --nodes 4 -p mycluster

# metric server
$minikube addons enable metrics-server --profile=mycluster
 
# make profile active: 

$minikube profile list

$minikube profile mycluster
- minikube profile was successfully set to mycluster

# Set Labels

$kubectl label nodes mycluster-m02 type=application
$kubectl label nodes mycluster-m03 type=dependent_services
$kubectl label nodes mycluster-m04 type=observability

#check lables

$kubectl get nodes --show-labels

# Create the taint for respective labels (node.yaml)**
Create the node.yaml file

# Generate the label for clusters
kubectl apply -f node.yaml

# Describe nodes info with labels
kubectl describe node mycluster-m02

```

**Steps:4  Create the namespace: (file: namespace.yaml)**

```bash
# create the namespace.yaml file for create the namespace.

# Apply the manifest

$kubectl apply -f namespaces.yaml

# Get the manifest output.
kubectl get namespaces

```

### Vault Setup: Control Flow with vault

**Steps:5  Create the vault container (File: vault.yaml)**

```bash
# Create the vault.yaml file
   
# Apply the vauly manifest
$kubctl apply -f vault.yaml

# Configure the  vault pod, Enter in pod and run all commands to setup the vault

$kubectl exec -it <pod-name> -n <namespace> -- /bin/sh

# initialize the vault & get the unseal key and root token
$vault operator init
 
# unseal the vault to use the unseal key.as below.
$vault operator  unseal-1 
$vault operator  unseal-2 
$vault operator  unseal-3 

# status vault
$vault status

# vault login 
$vault login Root-Token

# enable seacrets 
$vault secrets enable -path=secret kv 


# add secrets 
$vault kv put secret/<your-secrets>
$vault kv put secret/<your-secrets>
$vault kv put secret/<your-secrets>
$vault kv put secret/<your-secrets>
$vault kv put secret/<your-secrets>
      
# verify the secrets
$vault kv get secret/mysql
  
# Check the path and type
$vault auth list

# Verification in vault pod
$vault list secret/

# Access the vault on browser

# port forwaring:

$ kubectl port-forward service/<service-name> 8200:8200 -n vault &

# access on browser : http://127.0.0.1:8200/ & put the user as root and root token : <root-token>

```

### External Secrets configuration

**Step:6 External-Secrets configuration:**

```bash
#Create the token-secrets**
$kubectl create secret generic vault-token \
  --from-literal=token=<root-token> \
  -n student-api 
 
# VERIFY IF THE SECRETS WERE CREATED IN EXTERNAL-SECRETS NAMESPACE
$kubectl get secrets -n student-api

# VALIDATE THE TOKEN HAS SUFFICIENT PERMISSIONS (we are using root however)
$kubectl exec -it <Vault-pod> -n vault -- vault token lookup <root-token>

# ESO installation :  Install from helm chart repository**
# Add repo :
$helm repo add external-secrets https://charts.external-secrets.io

#Install External Secrets Operator
$helm install external-secrets \
   external-secrets/external-secrets \
    -n external-secrets \
    --create-namespace \

#Verify the Installation
$kubectl get pods -n external-secrets

#Logs check 
$kubectl logs external-secrets-955bcb878-krc9b -n external-secrets

# Check Custom Resource Definitions (CRDs)**
$kubectl get crd | grep externalsecrets

# create the externalsecrets.yaml
FileName: externalsecret.yaml

Note :  All secrets must me same name with vault secrets other wise its give the sync issue.

Its maintains the syncing with the vault. what data need to  be fetch.

# Create the secretstore.yaml manifest
FileName: secretstore.yaml

- Note: This file store the data as kubernetes datastore. which sync by the externalsecrets.

# Validating SecretStore Resources in External Secrets Operator**

# Get the secrets store
$kubectl get secretstore -n student-api

# Secrets store in details
$kubectl get secretstore vault-secret-store -o yaml -n student-api

- its must be error free and showing the valid

# Manifest deployment.**
$kubectl apply -f external-secrets/secretstore.yaml -n student-api
secretstore.external-secrets.io/vault-backend configured

$kubectl apply -f external-secrets/externalsecret.yaml -n student-api
externalsecret.external-secrets.io/db-api-secret configured

# get secrets store:
$kubectl get secretstore -n student-api

# Verify the Vault Token
$kubectl get secret vault-token -n student-api -o yaml

- Working fine till now.
```

**Step:7 ESO configuration**

```bash
# Varification externalsecrets
$kubectl get externalsecrets  -n  student-api

# secrets store varifiacaiton 
$kubectl get secretstore  -n  student-api

- Note:  the secrets must be same as the your externalsecrets file.
```

---

### Database deployment

**Step:8 Generate the db.yml manifest.**

```bash
# create the db.yml
# deployment of db.yaml
$kubectl apply -f api/db.yaml -n student-api

#Check pod status.
$kubectl get pods -n student-api

#Check the logs
$kubectl logs  db-deployment-b79b44ff9-kbb7g -n student-api

#Description of pod:
$kubectl describe pods db-deployment-b79b44ff9-kbb7g -n student-api

#Enter inside the the db pod.
$kubectl exec -it db-deployment-b79b44ff9-kbb7g -n student-api -- /bin/sh

# inside the pod check  the database login and details
# login in mysql

sh-5.1# mysql -u root -p
Enter password: 

```

### API deployment

**Step: 9 Generate the api.yml manifest.**

- NOTE: Generate the application docker image and push to your repository.
- API image do not have any migration. we can override the migration command using the init container.**

```bash
# create the api.yml manifest
# apply the api manifest
$kubectl apply -f api/api.yaml -n student-api

#all resources in student-api namespace.
$kubectl get all -n student-api

- NOTE :  First the run the into container and then run the API container.

# Check the description of the application and init container.
$kubectl describe pod/api-deployment-7947d4db87-5cgdz -n student-api

# Check the logs of the application container
$kubectl logs api-deployment-7947d4db87-5cgdz -n student-api

#Port forwarding
$kubectl port-forward service/api-service 5000:5000 -n student-api &

# After port forwarding we can check the application on browser.
- http://127.0.0.1:5000/healthcheck 

# Enter inside the API pod.
$kubectl exec -it pod/api-deployment-696479d9d9-vd27n -n student-api -- /bin/sh

# Check the live logs for application**
$kubectl logs -n student-api api-deployment-696479d9d9-vd27n -f 

# Check the db pod for database and related tables.
$kubectl exec -it pod/db-deployment-8578ff468-qzqn8 -n student-api -- /bin/sh

```

### API Testing

**Step: 10 Testing the application with live logs**

```bash
# Check the live logs in pod
$kubectl logs pod/api-deployment-7947d4db87-5cgdz -n student-api -f 

# Testing on postman
- Open the postman & run URL

- Healthcheck end point :  [http://127.0.0.1:5000/healthcheck]

- Insert student Records. [http://127.0.0.1:5000/api/v1/students]

- Check all student records [http://127.0.0.1:5000/api/v1/students]

- Edit the existing records [http://127.0.0.1:5000/api/v1/students/2]

- Delete the records [http://127.0.0.1:5000/api/v1/students/1]

# Testing on browser
- Health check: http://127.0.0.1:5000/healthcheck

- All student records: http://127.0.0.1:5000/api/v1/students

- Records with student ID : http://127.0.0.1:5000/api/v1/students/4

- If there is no records found then error and logs .

```

### Expectation:  The following expectations should be met to complete this milestone

- All Kubernetes manifests should be committed in the same GitHub repository and should follow the proper directory structure.✅
- Each component (application, DB) should have a single manifest file, which has all the different Kubernetes components. For example, the application.yml file should contain - namespace, configMap, secret, deployment, and service, etc. i.e. all K8s resource definitions required for the application to be deployed on K8s. Similarly, database.yml file should contain similar K8s resource definition for running database container on K8s.✅
- DB DML migrations should run before you start the application pod, as an init container.✅
- Application and DB components should be deployed in `student-api` namespace. Similarly, other elements should be deployed in the respective namespace and on the appropriate node. Here’s the deployment diagram for reference.✅
- You need to use ConfigMaps for passing environment variables.✅
- DB credentials and other sensitive information should be injected using Kubernetes External Secrets Operator(ESO).✅
- Hashicorp Vault should be deployed in the Kubernetes cluster and configured to be used as a secret store for ESO.✅
- You need to expose the REST API using the K8s service.✅
- You should get status code 200 while making the request using Postman collection for different API endpoints.✅
