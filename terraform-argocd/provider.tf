terraform {
  required_version = "= 1.5.3"

  required_providers {
    argocd = {
      source  = "jojand/argocd"
      version = "2.3.2"
    }
  }
}

provider "argocd" {
  server_addr = "https://ab07dc410c0144f5a94e89a4075bb922-1287458243.us-east-1.elb.amazonaws.com/applications"
  username    = "admin"
  password    = "123456789"
}
