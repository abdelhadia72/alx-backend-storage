#!/usr/bin/env python3
""" File 101-students """


def top_students(mongo_collection):
    """
        function that returns all
        students sorted by average score
    """
    pipeline = [
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
