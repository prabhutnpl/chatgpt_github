# Building and Pushing an Image to GCP Artifact Registry

This guide outlines the steps to build and push a container image to GCP Artifact Registry using Podman. 

## Prerequisites

- Podman installed
- A GCP project with Artifact Registry API enabled
- GCP project ID

## Building the Image

1. Start the Podman machine:

    ```bash
    podman machine start
    ```

2. Build the container image and tag it with `chatbot:latest`:

    ```bash
    podman build -t chatbot:latest .
    ```

## Running the Image Locally

1. Run the container image locally with `podman run`:

    ```bash
    podman run -p 5000:5000 -e OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXX -e GITHUB_TOKEN=github_pat_XXXXXXXXXXXXXXXXX chatbot:latest
    ```

   Replace the `OPENAI_API_KEY` and `GITHUB_TOKEN` environment variables with your own values.

## Pushing the Image to GCP Artifact Registry

1. Create a GCP project and enable the Artifact Registry API.

2. Create a repository in the GCP Artifact Registry.

3. Authenticate with gcloud:

    ```bash
    gcloud auth login
    ```

4. Tag the local image with the GCP Artifact Registry location:

    ```bash
    podman tag SOURCE-IMAGE LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE:TAG
    ```

    Replace `SOURCE-IMAGE`, `PROJECT-ID`, `REPOSITORY`, and `TAG` with your own values.

5. Authenticate with GCP Artifact Registry:

    ```bash
    gcloud auth print-access-token | podman login -u oauth2accesstoken --password-stdin us-central1-docker.pkg.dev
    ```

6. Push the image to GCP Artifact Registry:

    ```bash
    podman push us-central1-docker.pkg.dev/your-project-id/your-repo-name/chatbot:latest --remove-signatures
    ```

    Replace `your-project-id` with your own project ID.

That's it! Your container image is now stored in GCP Artifact Registry and can be deployed to a GCP Kubernetes cluster or used by other GCP services.