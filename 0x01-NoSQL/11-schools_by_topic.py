#!/usr/bin/env python3
""" find """


def schools_by_topic(mongo_collection, topic):
    """ find documents"""
    return [i for i in mongo_collection.find({"topics": topic})]
