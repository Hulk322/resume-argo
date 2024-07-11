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
sync_policy {
      automated = {
        prune       = true
        self_heal   = true
        allow_empty = true
      }
      # Only available from ArgoCD 1.5.0 onwards
      sync_options = ["Validate=false"]
      retry {
        limit   = "5"
        backoff = {
          duration     = "30s"
          max_duration = "2m"
          factor       = "2"
        }
      }
    }

    ignore_difference {
      group         = "apps"
      kind          = "Deployment"
      json_pointers = ["/spec/replicas"]
    }

    ignore_difference {
      group         = "apps"
      kind          = "StatefulSet"
      name          = "someStatefulSet"
      json_pointers = [
        "/spec/replicas",
        "/spec/template/spec/metadata/labels/bar",
      ]
    Only available from ArgoCD 2.1.0 onwards
      jq_path_expressions = [
        ".spec.replicas",
        ".spec.template.spec.metadata.labels.bar",
      ]
  }
}
