output "s3_bucket_name" {
  value       = aws_s3_bucket.omnistream_media.id
  description = "Name of the primary media storage S3 bucket"
}

output "kafka_bootstrap_brokers" {
  value       = aws_msk_cluster.omnistream_kafka.bootstrap_brokers_tls
  description = "TLS bootstrap broker connection strings for MSK Kafka cluster"
}

output "redis_endpoint" {
  value       = aws_elasticache_cluster.omnistream_redis.cache_nodes[0].address
  description = "Redis endpoint for caching and rate limiting"
}
