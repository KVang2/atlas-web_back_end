#!/usr/bin/env python3
""" list all documents in python """
import pymongo

def list_all(mongo_collection):
    """ Lists all documents """
    if mongo_collection.count_documents({}) == 0:
        return []

    return list(mongo_collection.find())
