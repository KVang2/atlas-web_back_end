#!/usr/bin/env python3
""" Insert new documents in python """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    mongo collection, pymongo collection object
    Returns: new id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
