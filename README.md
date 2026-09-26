# AWS Migration Toolkit

Portfolio project simulating a real cloud migration workflow: EC2 → ECS → EKS, with serverless and IaC best practices — built to cover the technical stack flagged as priority for an upcoming Cloud Migration & Transformation apprenticeship.

## Architecture

- **Compute progression**: EC2 (legacy baseline) → ECS Fargate (containerized) → EKS (target platform)
- **Kubernetes**: Deployment, Service, Ingress, ConfigMap, Secret, HorizontalPodAutoscaler — all tested locally with `kind`
- **Serverless**: Lambda triggered by S3 events, writing to DynamoDB
- **Storage & data**: S3 (uploads + Terraform state backend), DynamoDB (app data + Terraform lock)
- **IaC**: Terraform, modular (network / ec2 / ecs / eks / lambda / dynamodb / s3)
- **CI/CD**: GitHub Actions — Terraform validation across all modules

## Repository structure

\`\`\`
terraform/
  bootstrap/       # S3 + DynamoDB state backend
  modules/         # one module per AWS service
  environments/    # environment-specific composition
k8s/
  base/            # Deployment, Service, Ingress, ConfigMap, Secret, HPA
lambda/
  src/             # function code
  tests/           # pytest unit tests
.github/workflows/ # CI pipelines
\`\`\`

## Status

- [x] Terraform modules for EC2, ECS, EKS, Lambda, DynamoDB, S3, network
- [x] Kubernetes manifests validated locally (kind)
- [x] Lambda function with unit tests
- [x] CI pipeline validating all Terraform modules
- [ ] Live deployment to AWS (pending account verification)

## Why this project

Built to demonstrate hands-on readiness on the exact stack requested ahead of a Cloud Migration & Transformation apprenticeship: AWS (EC2/ECS/EKS/Lambda/DynamoDB/S3), core Kubernetes objects, Terraform, and GitHub Actions as the sole CI/CD tool.
