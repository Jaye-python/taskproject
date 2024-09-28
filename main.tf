terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "af-south-1"
}

# Create a new VPC
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  assign_generated_ipv6_cidr_block = true # use ipv6 to avoid charges

  tags = {
    Name = "Main VPC"
  }
}


# Create a public subnet
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  ipv6_cidr_block         = aws_vpc.main.ipv6_cidr_block # add the ipv6 cidr block to prevent charges
  assign_ipv6_address_on_creation = true # add the ipv6 cidr block to prevent charges
  # map_public_ip_on_launch = true
  availability_zone       = "af-south-1a"

  tags = {
    Name = "public_subnet"
  }
}

# add the ipv6  internet gateway to prevent charges
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "IPv6 Internet Gateway"
  }
}

# Create a new route table with ipv6 to prevent charges
resource "aws_route_table" "main" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  route {
    ipv6_cidr_block = "::/0"
    gateway_id      = aws_internet_gateway.main.id
  }

  tags = {
    Name = "IPv6 Route Table"
  }
}

# Associate the route table with the public subnet to avoid charges
resource "aws_route_table_association" "main" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.main.id
}


# Create a new security group
resource "aws_security_group" "app_server_sg" {
  name        = "app_server_sg"
  description = "Security group for app server"
  vpc_id      = aws_vpc.main.id

  # SSH access from your IP
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.my_ip]
  }

  # Jenkins port
  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = [var.my_ip] # cidr_blocks = ["0.0.0.0/0"]
  }

  # SSH access for AWS Connect
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["3.0.0.0/16", "3.1.0.0/16"]
  }

  # Django port
  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = [var.my_ip]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "app_server_sg"
  }
}

data "aws_ssm_parameter" "DATABASE_PASS" {
  name = "DATABASE_PASS"
}

resource "aws_instance" "app_server" {
  ami                    = var.ami
  instance_type          = "t3.micro"
  key_name               = var.key_pair_name
  vpc_security_group_ids = [aws_security_group.app_server_sg.id]
  subnet_id              = aws_subnet.public_subnet.id
  associate_public_ip_address = true

  credit_specification {
    cpu_credits = "standard" #default is 'unlimited' which incurs charges
  }

  tags = {
    Name = var.server_name
  }
}

# Create a security group for the RDS instance
resource "aws_security_group" "rds_sg" {
  name        = "rds-sg"
  description = "Security group for RDS instance"
  vpc_id      = aws_vpc.main.id

  # Allow traffic from the EC2 security group
  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.app_server_sg.id]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }

  tags = {
    Name = "RDS Security Group"
  }
}

# Create a DB Subnet Group
resource "aws_db_subnet_group" "main" {
  name       = "main-db-subnet-group"
  subnet_ids = [aws_subnet.public_subnet.id]

  tags = {
    Name = "main-db-subnet-group"
  }
}

resource "aws_db_instance" "default" {
  allocated_storage       = 20
  identifier              = var.db_name
  db_name                 = var.db_name
  engine                  = "postgres"
  instance_class          = "db.t3.micro"
  username                = "postgres"
  password                = data.aws_ssm_parameter.DATABASE_PASS.value
  skip_final_snapshot     = true
  max_allocated_storage   = 0
  backup_retention_period = 0 # default is 35 days which incurs charges
  db_subnet_group_name    = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.rds_sg.id]
  

}


# Save the RDS endpoint to SSM Parameter Store
resource "aws_ssm_parameter" "database_host" {
  name      = "DATABASE_HOST"
  type      = "String"
  value     = aws_db_instance.default.endpoint
  # overwrite = true
}

# Update the ALLOWED_HOSTS parameter in SSM
resource "aws_ssm_parameter" "allowed_hosts" {
  name      = "ALLOWED_HOSTS"
  type      = "String"
  value     = aws_instance.app_server.public_ip
  # overwrite = true
}

