import redis.asyncio as redis
import json
import logging
from typing import Optional, Any

from app.config import settings

logger = logging.getLogger(__name__)
redis_client: Optional[redis.Redis] = None

async def init_cache():
    """Initialize Redis connection."""
    global redis_client
    try:
        redis_client = redis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True
        )
        await redis_client.ping()
        logger.info("Redis connected")
    except Exception as e:
        logger.error(f"Redis connection failed: {e}")
        redis_client = None

async def cache_get(key: str) -> Optional[Any]:
    """Get value from cache."""
    if not redis_client:
        return None
    try:
        value = await redis_client.get(key)
        return json.loads(value) if value else None
    except Exception as e:
        logger.error(f"Cache get error: {e}")
        return None

async def cache_set(key: str, value: Any, ttl: int = 300):
    """Set value in cache with TTL."""
    if not redis_client:
        return
    try:
        await redis_client.setex(key, ttl, json.dumps(value, default=str))
    except Exception as e:
        logger.error(f"Cache set error: {e}")