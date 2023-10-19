#!/usr/bin/env python3
"""
insert module
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection
    Arguments:
        mongo_collection - the target collection
        kwargs - the data to be inserted in the mongo_collection
    """
    # _id = mongo_collection.insert_one(kwargs)
    # for the version in the ALX checker server
    _id = mongo_collection.insert(kwargs)
    return _id
