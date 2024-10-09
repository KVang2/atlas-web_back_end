#!/usr/bin/env python3
""" Return list of school with special topic """
from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    