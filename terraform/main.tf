
resource "google_service_account" "cloudrun-service-account" {
  account_id   = "sa-cloudrun"
  display_name = "CloudRun Service Account"
  project = "ai-chatbot-386317"
}

resource "google_project_iam_member" "roles" {
for_each = toset([
    "roles/run.developer",
    "roles/secretmanager.secretAccessor",
    "roles/artifactregistry.reader",
  ])
  role    = each.key
  member = "serviceAccount:${google_service_account.cloudrun-service-account.email}"
  project = "ai-chatbot-386317"
  depends_on = [google_service_account.cloudrun-service-account]
}

#enable the cloudrun api

resource "google_project_service" "run_api" {
  project = "ai-chatbot-386317"
  service = "run.googleapis.com"

  disable_on_destroy = true
  depends_on = [google_project_iam_member.roles]
}

resource "google_cloud_run_service" "chatbot" {
  name     = "ai-chatbot"
  project  = "ai-chatbot-386317"
  location = "us-central1"

  template {
    spec {
      service_account_name = "${google_service_account.cloudrun-service-account.email}"
      containers {
        image = "us-central1-docker.pkg.dev/ai-chatbot-386317/ai-chatbot/chatbot:latest"
        ports {
          container_port = 5000
        }
        env {
          name = "OPENAI_API_KEY"
          value_from {
            secret_key_ref {
              name = "OPENAI_API_KEY"
              key  = "latest"
            }
          }
        }

        env {
          name = "GITHUB_TOKEN"
          value_from {
            secret_key_ref {
              name = "GITHUB_TOKEN"
              key  = "latest"
            }
          }
        }
      }
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
  depends_on = [google_project_service.run_api]
}

resource "google_cloud_run_service_iam_member" "run_all_users" {

  service  = google_cloud_run_service.chatbot.name
  location = google_cloud_run_service.chatbot.location
  role     = "roles/run.invoker"
  member   = "allUsers"
  project  = google_cloud_run_service.chatbot.project

}

