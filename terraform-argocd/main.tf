resource "argocd_application" "app" {
  metadata {
    name      = "resume"
    namespace = "argocd"
    labels = {
      test = "true"
    }
  }

  spec {
    project = "default"

    source {
      repo_url        = "https://github.com/Hulk322/resume-argo.git"
      path            = "."
      target_revision = "HEAD"
    }

    destination {
      name      = "in-cluster"
      namespace = "argocd"
    }
  }
}
