provider "aws" {
  region = "us-east-1"
}

resource "aws_ecs_cluster" "cluster" {
  name = "smart-agro-hub-cluster"
}

resource "aws_ecs_task_definition" "task" {
  family                   = "smart-agro-hub-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "512"
  memory                   = "1024"

  container_definitions = jsonencode([{
    name      = "api"
    image     = "your-registry/smart-agro-hub:latest"
    essential = true
    portMappings = [{
      containerPort = 80
      hostPort      = 80
    }]
  }])
}

resource "aws_ecs_service" "service" {
  name            = "smart-agro-hub-service"
  cluster         = aws_ecs_cluster.cluster.id
  task_definition = aws_ecs_task_definition.task.arn
  desired_count   = 2
  launch_type     = "FARGATE"
  network_configuration {
    subnets         = ["subnet-xxxxxxxx"]
    security_groups = ["sg-xxxxxxxx"]
  }
}
