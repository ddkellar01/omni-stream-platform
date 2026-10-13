resource "aws_elasticache_subnet_group" "redis_subnet" {
  name       = "omnistream-redis-subnet"
  subnet_ids = ["subnet-xxxxxx1", "subnet-xxxxxx2"]
}

resource "aws_elasticache_cluster" "omnistream_redis" {
  cluster_id           = "omnistream-redis-cache"
  engine               = "redis"
  node_type            = "cache.t4g.medium"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis7"
  engine_version       = "7.0"
  port                 = 6379
  subnet_group_name    = aws_elasticache_subnet_group.redis_subnet.name
}
