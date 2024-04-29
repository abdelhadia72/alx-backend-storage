#!/usr/bin/env python3
"""
    lists all documents in a collection
"""

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client.my_db
collection = database.school

for doc in collection.find():
    """
    function loops on all documents and print them
    """
    if doc:
        return(doc)
    return []

