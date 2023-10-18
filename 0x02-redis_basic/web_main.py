#!/usr/bin/env python3
"""
test web cache module
"""
from web import get_page
import redis


get_page("http://google.com")

r = redis.Redis()

print(r.get("count:http://google.com"))