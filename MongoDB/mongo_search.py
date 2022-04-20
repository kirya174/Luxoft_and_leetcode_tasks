from bson import ObjectId
import config
import pymongo
from pymongo import MongoClient


def print_all():
    with MongoClient(config.mongodb) as client:
        db = client[config.database]
        entities = db.entities
        for entity in entities.find():
            print(f"firstname = {entity['first_name']}, lastname = {entity['last_name']}")


def print_document_by_id(id):
    query = {'_id': ObjectId(id)}
    with MongoClient(config.mongodb) as client:
        db = client[config.database]
        entities = db.entities
        entity = entities.find_one(query)
        print(entity)
        print(f"firstname = {entity['first_name']}, lastname = {entity['last_name']}")
        

print_all()
print_document_by_id("625e6ad796fbe33ab57144aa")
print_document_by_id("625e6ad796fbe33ab57144ac")