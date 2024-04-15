#!/usr/bin/env python3
""" list """

import pymongo


def list_all(mongo_collection):
    """ List all elements in a collection """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
