# Kubernetes Local Development Setup Guide

This guide provides step-by-step instructions for setting up a local Kubernetes development environment using kind (Kubernetes in Docker) and kubectl on any system.

## Prerequisites

- Docker installed and running
- Administrative/sudo access
- Internet connection for downloading tools

## Step 1: Install Docker (if not already installed)

### Ubuntu/Debian
```bash
# Update package index
sudo apt-get update

# Install required packages
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Add user to docker group (requires logout/login)
sudo usermod -aG docker $USER
```

### CentOS/RHEL/Fedora
```bash
# Install Docker
sudo dnf install -y docker

# Start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group
sudo usermod -aG docker $USER
```

### macOS
```bash
# Install Docker Desktop from https://docs.docker.com/desktop/mac/install/
# Or using Homebrew:
brew install --cask docker
```

### Windows
- Download Docker Desktop from https://docs.docker.com/desktop/windows/install/
- Follow the installation wizard

## Step 2: Install kubectl

### Linux
```bash
# Download the latest kubectl binary
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Make it executable
chmod +x kubectl

# Move to PATH
sudo mv kubectl /usr/local/bin/

# Verify installation
kubectl version --client
```

### macOS
```bash
# Using Homebrew (recommended)
brew install kubectl

# Or download binary directly
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

### Windows
```powershell
# Using Chocolatey
choco install kubernetes-cli

# Or using Scoop
scoop install kubectl

# Or download binary from:
# https://dl.k8s.io/release/v1.28.0/bin/windows/amd64/kubectl.exe
```

## Step 3: Install kind

### Linux
```bash
# Download kind binary
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64

# Make it executable
chmod +x ./kind

# Move to PATH
sudo mv ./kind /usr/local/bin/kind

# Verify installation
kind version
```

### macOS
```bash
# Using Homebrew (recommended)
brew install kind

# Or download binary directly
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-darwin-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

### Windows
```powershell
# Using Chocolatey
choco install kind

# Or using Scoop
scoop install kind

# Or download from: https://kind.sigs.k8s.io/dl/v0.20.0/kind-windows-amd64
```

## Step 4: Create a Kubernetes Cluster

### Basic cluster creation
```bash
# Create a new cluster named "akscli-test"
kind create cluster --name akscli-test

# Verify cluster is running
kubectl cluster-info --context kind-akscli-test

# Check nodes
kubectl get nodes
```

### Advanced cluster configuration (optional)
Create a `kind-config.yaml` file for more control:

```yaml
# kind-config.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
- role: worker
- role: worker
```

Then create cluster with config:
```bash
kind create cluster --name akscli-test --config kind-config.yaml
```

## Step 5: Set up kubectl context

```bash
# Set the current context to your kind cluster
kubectl config use-context kind-akscli-test

# Verify you can access the cluster
kubectl get namespaces

# Check cluster info
kubectl cluster-info
```

## Step 6: Deploy Test Workloads (for akscli testing)

Create a test manifest file `test-k8s-setup.yaml`:

```yaml
# Create test namespaces
apiVersion: v1
kind: Namespace
metadata:
  name: production
---
apiVersion: v1
kind: Namespace
metadata:
  name: staging
---
apiVersion: v1
kind: Namespace
metadata:
  name: development
---

# Test web application in default namespace
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  namespace: default
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web
        image: nginx:alpine
        ports:
        - containerPort: 80
        env:
        - name: NODE_ENV
          value: "development"
        - name: PORT
          value: "80"
        command: ["sh", "-c", "while true; do echo '[WEB] Server running on port 80'; sleep 30; done"]
---

# Multi-container pod in production namespace
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-server
  namespace: production
spec:
  replicas: 1
  selector:
    matchLabels:
      app: api-server
  template:
    metadata:
      labels:
        app: api-server
    spec:
      containers:
      - name: api
        image: nginx:alpine
        command: ["sh", "-c", "while true; do echo '[API] Server running on port 8080'; sleep 30; done"]
      - name: sidecar
        image: alpine:latest
        command: ["sh", "-c", "while true; do echo '[SIDECAR] Health check passed'; sleep 60; done"]
---

# Database pod in staging namespace
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres-db
  namespace: staging
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres-db
  template:
    metadata:
      labels:
        app: postgres-db
    spec:
      containers:
      - name: postgres
        image: alpine:latest
        command: ["sh", "-c", "while true; do echo '[DB] Database connection established'; sleep 45; done"]
---

# Worker pod in development namespace
apiVersion: apps/v1
kind: Deployment
metadata:
  name: background-worker
  namespace: development
spec:
  replicas: 1
  selector:
    matchLabels:
      app: background-worker
  template:
    metadata:
      labels:
        app: background-worker
    spec:
      containers:
      - name: worker
        image: alpine:latest
        command: ["sh", "-c", "while true; do echo '[WORKER] Processing jobs...'; sleep 20; done"]
```

Deploy the test workloads:
```bash
# Apply the test manifest
kubectl apply -f test-k8s-setup.yaml

# Wait for pods to be ready
kubectl wait --for=condition=ready pod --all --timeout=300s

# Verify deployments
kubectl get pods --all-namespaces
kubectl get namespaces
```

## Useful Commands for Management

### Cluster Management
```bash
# List all kind clusters
kind get clusters

# Delete a cluster
kind delete cluster --name akscli-test

# Load a Docker image into kind cluster
kind load docker-image my-app:latest --name akscli-test

# Export kubeconfig
kind export kubeconfig --name akscli-test
```

### kubectl Context Management
```bash
# List all contexts
kubectl config get-contexts

# Switch context
kubectl config use-context kind-akscli-test

# Get current context
kubectl config current-context

# View cluster info
kubectl cluster-info
```

### Debugging and Monitoring
```bash
# Get all resources in all namespaces
kubectl get all --all-namespaces

# Describe a problematic pod
kubectl describe pod <pod-name> -n <namespace>

# Get pod logs
kubectl logs <pod-name> -n <namespace>

# Execute into a pod
kubectl exec -it <pod-name> -n <namespace> -- /bin/sh

# Port forward to access services locally
kubectl port-forward svc/<service-name> 8080:80 -n <namespace>
```

## Cleanup

```bash
# Delete test workloads
kubectl delete -f test-k8s-setup.yaml

# Delete the kind cluster
kind delete cluster --name akscli-test

# Remove Docker containers and images (optional)
docker system prune -a
```

## Troubleshooting

### Docker Issues
- Ensure Docker is running: `docker ps`
- Check Docker permissions: `docker run hello-world`
- Restart Docker service: `sudo systemctl restart docker`

### kind Issues
- Check cluster status: `kind get clusters`
- View cluster logs: `kind export logs --name akscli-test`
- Recreate cluster if corrupted: `kind delete cluster --name akscli-test && kind create cluster --name akscli-test`

### kubectl Issues
- Verify context: `kubectl config current-context`
- Check connectivity: `kubectl cluster-info`
- Reset context: `kind export kubeconfig --name akscli-test`

## Next Steps

1. **Customize the test workloads** to match your specific testing needs
2. **Set up CI/CD pipelines** that use this local cluster for testing
3. **Add ingress controllers** for more realistic web application testing
4. **Configure persistent volumes** for stateful application testing
5. **Install monitoring tools** like Prometheus and Grafana for observability testing

This setup provides a fully functional local Kubernetes environment that closely mirrors production clusters, perfect for developing and testing CLI tools like akscli.
