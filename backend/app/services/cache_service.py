"""Cache Service - Redis Integration"""

import json
import logging
from typing import Any, Optional

import redis
from redis.asyncio import Redis

from app.config import settings

logger = logging.getLogger(__name__)


class CacheService:
    """Redis Cache Service"""

    def __init__(self, redis_url: str = settings.REDIS_URL):
        """Initialize cache service"""
        self.redis_url = redis_url
        self.client: Optional[Redis] = None

    async def connect(self) -> None:
        """Connect to Redis"""
        try:
            self.client = redis.from_url(
                self.redis_url,
                encoding="utf8",
                decode_responses=True,
            )
            await self.ping()
            logger.info("Connected to Redis")
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
            raise

    async def disconnect(self) -> None:
        """Disconnect from Redis"""
        if self.client:
            await self.client.close()
            logger.info("Disconnected from Redis")

    async def ping(self) -> bool:
        """Ping Redis to check connection"""
        try:
            if self.client:
                result = await self.client.ping()
                return result
            return False
        except Exception as e:
            logger.error(f"Redis ping failed: {e}")
            return False

    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache"""
        try:
            if not self.client:
                return None
            value = await self.client.get(key)
            if value:
                return json.loads(value)
            return None
        except Exception as e:
            logger.error(f"Cache get error for key {key}: {e}")
            return None

    async def set(
        self,
        key: str,
        value: Any,
        ttl: int = settings.REDIS_CACHE_TTL,
    ) -> bool:
        """Set value in cache"""
        try:
            if not self.client:
                return False
            await self.client.setex(
                key,
                ttl,
                json.dumps(value, default=str),
            )
            return True
        except Exception as e:
            logger.error(f"Cache set error for key {key}: {e}")
            return False

    async def delete(self, key: str) -> bool:
        """Delete value from cache"""
        try:
            if not self.client:
                return False
            await self.client.delete(key)
            return True
        except Exception as e:
            logger.error(f"Cache delete error for key {key}: {e}")
            return False

    async def clear(self) -> bool:
        """Clear all cache"""
        try:
            if not self.client:
                return False
            await self.client.flushdb()
            return True
        except Exception as e:
            logger.error(f"Cache clear error: {e}")
            return False


# Global cache service instance
cache_service = CacheService()
