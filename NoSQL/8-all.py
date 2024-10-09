#!/usr/bin/env python3
""" list all documents in python """
from pymongo import MongoClient

def list_all(mongo_collection):
    """ Lists all documents """
    return mongo_collection.find()
