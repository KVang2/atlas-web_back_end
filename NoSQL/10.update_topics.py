#!/usr/bin/env python3
""" Change topics of school document """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """ updating topics """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
