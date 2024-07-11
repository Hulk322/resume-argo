terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.10.0"
    }
    argocd = {
      source  = "oboukili/argocd"
      version = "~> 3.0.0"
    }
  }

  required_version = ">= 1.0.0"
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

provider "argocd" {
  server_addr = "https://ab07dc410c0144f5a94e89a4075bb922-1287458243.us-east-1.elb.amazonaws.com"
  username    = "admin"
  password    = "123456789"
}
