#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from functools import wraps
import redis
from typing import Union, Callable, Optional, Any
import uuid


def count_calls(method: Callable) -> Callable:
    """creating a decorator"""
    @wraps(method)
    def wrapper_func(self, *args, **kwargs):
        """thhe inner function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper_func


class Cache:
    def __init__(self) -> None:
        """consructor of the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, stores the input data in Redis using random key
        returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Any:
        """
        retrives a data associated with key from redis db
        """
        data = self._redis.get(key)
        if fn and data:
            data = fn(data)
        return data

    def get_str(self, key: str, fn: Optional[Callable] = None) -> str:
        """
        retrives a data associated with key from redis db
        returns in the string format
        """
        return str(self.get(key, fn=fn))

    def get_int(self, key: str, fn: Optional[Callable] = None) -> int:
        """
        retrives a data associated with key from redis db
        returns in the string format
        """
        return int(self.get(key, fn=fn))
