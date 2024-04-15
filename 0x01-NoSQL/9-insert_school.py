#!/usr/bin/env python3
""" insert """


def insert_school(mongo_collection, **kwargs):
    """inserts in school collection a document"""
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
