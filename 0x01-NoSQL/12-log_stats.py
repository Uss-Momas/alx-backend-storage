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
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(count(nginx_collection)))
    print("Methods:")
    for method in methods:
        count_method = count(nginx_collection, method=method)
        print("\tmethod {}: {}".format(method, count_method))
    data = nginx_collection.find()
    print("{} status check".format(count(nginx_collection, method='GET',
                                         path='/status')))
