# vault-config.hcl

# Enable the listener
listener "tcp" {
  # Set the address to bind to; this allows Vault to accept incoming requests
  address = "0.0.0.0:8200"
  # Disabling TLS for simplicity; enable in production
  tls_disable = true
}

# Specify storage backend
storage "raft" {
  path = "/vault/data"
  
  # Specify the cluster address for Raft
  cluster_addr = "http://0.0.0.0:8201"  # Adjust this address as needed
}

# Define telemetry settings
#telemetry {
#  disable = false  # Keep telemetry enabled
#}
