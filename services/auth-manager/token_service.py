import os
from cryptography.fernet import Fernet
import redis

REDIS_URL = os.getenv("REDIS_URL", "redis://redis-cache:6379")
ENCRYPTION_KEY = os.getenv("FERNET_KEY", Fernet.generate_key())
cipher = Fernet(ENCRYPTION_KEY)
r = redis.Redis.from_url(REDIS_URL)

def store_token(platform: str, user_id: str, access_token: str):
    encrypted_token = cipher.encrypt(access_token.encode())
    r.set(f"token:{platform}:{user_id}", encrypted_token)

def retrieve_token(platform: str, user_id: str) -> str:
    encrypted_token = r.get(f"token:{platform}:{user_id}")
    if not encrypted_token:
        raise ValueError("Token not found or expired")
    return cipher.decrypt(encrypted_token).decode()
