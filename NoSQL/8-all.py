//  devuelve todos los documentos de una colección MongoDB usando PyMongo
#!/usr/bin/env python3
"""Function that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        A list of documents (or empty list if no documents exist)
    """
    return list(mongo_collection.find())
