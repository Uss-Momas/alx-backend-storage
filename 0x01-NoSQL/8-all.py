#!/usr/bin/env python3
"""
all module
retrieves data from mongoDB
"""


def list_all(mongo_collection):
    """
    function to list all documents in a collection
    """
    return list(mongo_collection.find())
