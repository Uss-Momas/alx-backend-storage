#!/usr/bin/env python3
"""
logs stats module
"""
from pymongo import MongoClient


def count(mongo_collection, **filter_args):
    """
    counts the number of documents of a collection
    Args:
        mongo_collection - pymongo collection cursor
        filter_args - a dictionaire of named variables params
    """
    return mongo_collection.count_documents(filter_args)


if __name__ == '__main__':
    """some stats about Nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    count_logs = count(nginx_collection)
    print(f"{count_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count_method = count(nginx_collection, method=method)
        print(f"\tmethod {method}: {count_method}")
    status_ch = count(nginx_collection, method='GET', path='/status')
    print(f"{status_ch} status check")
