#!/usr/bin/env python3
"""Inserts doc into a collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserts doc into a collection"""
    
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
