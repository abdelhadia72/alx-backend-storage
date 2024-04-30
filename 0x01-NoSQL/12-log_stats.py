#!/usr/bin/env python3
""" File 12-log_stats.py """

from pymongo import MongoClient


def log_stats():
    """ Python script that provides some stats
    about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count_documents({})

    methods_count = {
        "GET": nginx_collection.count_documents({"method": "GET"}),
        "POST": nginx_collection.count_documents({"method": "POST"}),
        "PUT": nginx_collection.count_documents({"method": "PUT"}),
        "PATCH": nginx_collection.count_documents({"method": "PATCH"}),
        "DELETE": nginx_collection.count_documents({"method": "DELETE"})
    }

    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in methods_count.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
