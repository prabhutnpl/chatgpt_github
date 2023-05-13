# Terraform Deployment for Google Cloud Run Service

This Terraform code deploys a Cloud Run service on Google Cloud Platform, running a chatbot application that uses environment variables to authenticate with external services. 

## Prerequisites

Before deploying this Terraform code, you need to have the following:

- A Google Cloud Platform account
- A Google Cloud project
- The [Google Cloud SDK](https://cloud.google.com/sdk) installed and configured on your machine
- The [Terraform CLI](https://www.terraform.io/downloads.html) installed on your machine

## Usage

1. Push your Docker image for the chatbot application to a container registry accessible to Terraform. This code assumes that the image is stored in the `us-central1-docker.pkg.dev` registry, with the repository name `ai-chatbot/chatbot`.

2. Clone this repository and navigate to the terraform folder containing the `main.tf` file.

3. In `main.tf`, replace `your-project-id` with your Google Cloud project ID.

4. In your terminal, run the following commands to deploy the Cloud Run service:

   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

5. Once the Terraform deployment is complete, access the URL for the Cloud Run service to test the chatbot application.

## Files

This repository contains the following file:

- `main.tf`: Contains the Terraform code for creating the Cloud Run service, IAM roles, and permissions.

## References

- [Cloud Run Documentation](https://cloud.google.com/run/docs/)
- [Terraform Google Cloud Platform Provider Documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs)