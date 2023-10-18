#!/usr/bin/env python3
"""
web cache module
"""
from functools import wraps
import requests
import redis
from typing import Callable


def count_access(method: Callable) -> Callable:
    """count the number of access a page has had"""
    @wraps(method)
    def wrapper_fun(*args, **kwargs):
        """the wrapper function"""
        r = redis.Redis()
        url = args[0]
        key = f"count:{url}"
        r.incr(key)
        return method
    return wrapper_fun


@count_access
def get_page(url: str) -> str:
    """uses requests module to obtain HTML content of a URL and returns it"""
    content = requests.get(url)
    return content.text
