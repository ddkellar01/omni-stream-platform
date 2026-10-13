resource "aws_db_subnet_group" "omnistream_db_subnet" {
  name       = "omnistream-db-subnet-group"
  subnet_ids = ["subnet-xxxxxx1", "subnet-xxxxxx2"]
}

resource "aws_db_instance" "omnistream_postgres" {
  identifier             = "omnistream-metadata-db"
  engine                 = "postgres"
  engine_version         = "15.4"
  instance_class         = "db.t4g.medium"
  allocated_storage      = 50
  max_allocated_storage  = 500
  db_name                = "omnistream"
  username               = "admin"
  password               = "ChangeMeInProductionSecurePassword!"
  db_subnet_group_name   = aws_db_subnet_group.omnistream_db_subnet.name
  skip_final_snapshot    = true
}
