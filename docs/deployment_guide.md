# Deployment Guide

## Heroku Deployment
1. Install Heroku CLI.
2. `heroku login`
3. `heroku create smart-agro-hub`
4. `git push heroku main`
5. `heroku open`

## Terraform Deployment (AWS ECS)
1. Install Terraform and AWS CLI.
2. `terraform init` in `deployment/terraform`.
3. Configure AWS credentials.
4. `terraform apply`.
