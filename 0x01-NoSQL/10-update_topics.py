#!/usr/bin/env python3
""" File 10-update_topics.py """


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a school document based on the name"""
    filter_query = {"name": name}
    update_query = {"$set": {"topics": topics}}

    result = mongo_collection.update_many(filter_query, update_query)
