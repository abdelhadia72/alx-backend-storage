#!/usr/bin/env python3
""" File 12-log_stats.py """

from pymongo import MongoClient


def log_stats():
    """ Python script that provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    print(f"{nginx_collection.count_documents({})} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {
              nginx_collection.count_documents({"method": method})}")
    print(f"{nginx_collection.count_documents(
        {"path": "/status"})} status check")


log_stats()
