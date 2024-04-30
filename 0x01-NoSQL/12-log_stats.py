#!/usr/bin/env python3
""" File 12-log_stats.py """

from pymongo import MongoClient


def log_stats():
    """
        Python script that provides some
        stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    print("{} logs".format(nginx_collection.count_documents({})))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count_method = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count_method))
    path_status = nginx_collection.count_documents({"path": "/status"})
    print("{} status check".format(path_status))


if __name__ == "__main__":
    log_stats()
