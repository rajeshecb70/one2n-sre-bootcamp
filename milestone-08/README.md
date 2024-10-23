**1. Project Title**

Deploy REST API & its dependent services using Helm Charts

**2. Project Description**

The project involves setup the REST API in kubernetes cluster using the helm.


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
$minikube start --nodes 2 -p mycluster

# custom resource 
$minikube start --cpus=2 --memory=4096 --nodes 4 -p mycluster

# metric server
$minikube addons enable metrics-server --profile=mycluster
 
# make profile active: 

$minikube profile list

$minikube profile cluster
- minikube profile was successfully set to mycluster

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

### 5. Vault Setup: Control Flow with vault

```bash
# Create the vaule.yaml file
   
# Apply the vault manifest using the helm.

$helm install vault hashicorp/vault --namespace vault -f app-charts/values.yaml

- Enable the engine 
- Store the secrets
- get the secrets.
- Enable and Access the Vault UI
```

```bash
$kubectl port-forward svc/vault-ui 8200:8200 -n vault &
```


### 6. Verify If The Secrets Were Created In External-secrets Namespace

```yaml
# Get the secrets  from student-api namespace
$kubectl get secrets -n student-api

# validation 
$kubectl get secrets vault-token -n student-api -o yaml
```

### 7. Installation External Secrets From Helm Chart

7.1 install external secrets

```yaml
$helm repo add external-secrets https://charts.external-secrets.io
"external-secrets" already exists with the same configuration, skipping

$helm install external-secrets \
   external-secrets/external-secrets \
    -n external-secrets \
    --create-namespace \

```

### 8. Create the API charts & configuration.

8.1. create the api-charts

```yaml
$helm create api-charts
```

8.2. create the secretstore template & values file

8.2.1. Generate the Helm Template

```yaml
$helm template api-charts  # To check the template syntax and errors.   
```

8.2.2. Deploy  the secretstore using the helm

```yaml
$helm install api ./api-charts --namespace student-api
```

8.2.3. validate the secrestore.

```yaml
$kubectl get secretstore -n student-api

#validate the vault-token.

$kubectl get secret vault-token -n student-api 


$kubectl describe secretstore vault-secret-store -n student-api

8.3 create the Externalsecrerts template & values file


# create file externalsecrets.yaml
# touch api-charts/templates/externalsecret.yaml

# deploy the helm 
$helm uninstall api --namespace student-api

# install the same.
$helm install api ./api-charts --namespace student-api
```



### 9. Create the database template and values.yaml

9.1. deploy the Database  helm charts

9.1.1 uninstall the exiting one and install the new

```yaml
$helm uninstall api --namespace student-api

```
9.1.2  install the new one

```yaml
# install the release 
$helm install api ./api-charts --namespace student-api
```


### 10. Create the api template and values.yaml.

10.1. deploy the API  helm charts

10.1.1 uninstall the exiting one and install the new

```yaml
$helm uninstall api --namespace student-api

```
10.1.2  install the new one

```yaml
# install the release 
$helm install api ./api-charts --namespace student-api
```

10.1.3 Access the API on browser.  Need to port forwarding. 

```yaml
# check the API service
$kubectl get svc -n student-api

#Port forwaring.
$kubectl port-forward service/api-service-new 5000:5000 -n student-api  &

# Check all endpoint on postmand. specially insert and update.

#Healtch check
http://127.0.0.1:5000/healthcheck

# Check all points.
http://127.0.0.1:5000/api/v1/students

```
### Expectations

The following expectations should be met to complete this milestone.
 - All helm charts should be committed in the GitHub repository and should follow the proper directory structure:✅
 - For services like DB & Hashicorp Vault, you can use community-managed charts, but it is recommended that you also add these charts inside the helm directory.✅
 - The entire stack should be running using Helm charts and not using the K8s manifest.✅
 - README.md should be updated with appropriate instructions for deploying our stack using these helm charts.✅