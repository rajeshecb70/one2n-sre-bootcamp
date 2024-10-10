## 1. Project Title

Milestone-06 : Setup Kubernetes cluster

## 2. Project Description

This project aims to set up kubernetes clusters to spun up three nodes using the minikube.

## 3. Prerequisites

- minikube
- Docker
- Virtualbox

## 4. Setup & configuration of milestone-04

```

# Clone the repository
git clone https://github.com/rajeshecb70/one2n-sre-bootcamp.git
cd one2n-sre-bootcamp/milestone-06
```

```
# Start minikube with three cluster nodes
minikube start --nodes=4
```

```
# Get the list of nodes
kubectl get nodes
```

output :
NAME           STATUS   ROLES           AGE     VERSION
minikube       Ready    control-plane   4m48s   v1.31.0
minikube-m02   Ready    <none>          4m37s   v1.31.0
minikube-m03   Ready    <none>          4m28s   v1.31.0
minikube-m04   Ready    <none>          4m16s   v1.31.0

```
# Set lables of related nodes
kubectl label node minikube-m02 type=application
kubectl label node minikube-m03 type=dependent_services
kubectl label node minikube-m04 type=observability
```

```
# show lables of related nodes
kubectl get nodes --show-labels
```

```
# Stop minikube 
minikube stop
```

```
# Delete minikube 
minikube delete
```

```
# Delete the all minikube
minikube delete --all
```

### 5. Expectations

- The following expectations should be met to complete this milestone.
- Three node Kubernetes cluster using Minikube should be spun up.✅
- Appropriate node labels should be added to these three nodes.
- Ex:
    Node A: type=application✅
    Node B: type=dependent_services✅
    Node C: type=observability✅  
