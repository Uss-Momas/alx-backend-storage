#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import redis
from typing import Union
import uuid


class Cache:
    def __init__(self) -> None:
        """consructor of the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, stores the input data in Redis using random key
        returns the key
        """
        key = uuid.uuid4()
        self._redis.set(key, data)
        return key
    