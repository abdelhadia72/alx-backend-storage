def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    """
    if mongo_collection.count_documents({}) == 0:
        return []
    return list(mongo_collection.find())