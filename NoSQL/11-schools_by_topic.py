#!/usr/bin/env python3
"""Module that contains the find by topic function"""


def schools_by_topic(mongo_collection, topic):
    """Function tha finds a school by topic"""
    
    return list(mongo_collection.find({'topics': topic}))
