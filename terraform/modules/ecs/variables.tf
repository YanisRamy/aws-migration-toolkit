variable "project_name" { type = string }
variable "vpc_id" { type = string }
variable "private_subnet_ids" { type = list(string) }
variable "region" { type = string }
variable "container_image" {
  type    = string
  default = "nginxdemos/hello:latest"
}
