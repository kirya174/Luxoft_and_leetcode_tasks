from bson import ObjectId
import config
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


def print_document_by_id_without_fields(id):
    query = {'_id': ObjectId(id)}
    with MongoClient(config.mongodb) as client:
        db = client[config.database]
        entities = db.entities
        entity = entities.find_one(query, {'_id': 0, 'first_name': 1, 'last_name': 1})
        print(entity)


def print_document_by_gt(age):
    query = {'age': {"$gt": age}}
    with MongoClient(config.mongodb) as client:
        db = client[config.database]
        entities = db.entities
        documents = entities.find(query)
        for document in documents:
            print(document)


def print_documents_by_multiple_conditions():
    query = {"$and": [{"age": {"$gt": 20, "$lt": 45}},
                      {"first_name": {"$eq": "Ivan"}}]}
    with MongoClient(config.mongodb) as client:
        db = client[config.database]
        entities = db.entities
        documents = entities.find(query)
        for document in documents:
            print(document)


def increase_age(id):
    search_query = {'_id': ObjectId(id)}
    with MongoClient(config.mongodb) as client:
        db = client[config.database]
        entities = db.entities
        document = entities.find_one(search_query)
        print(document)
        update_query = {"$set":
                            {"age": document["age"] + 1}}
        entities.update_one(search_query, update_query)
        updated_document = entities.find_one(search_query)
        print(updated_document)


if __name__ == '__main__':
    print_all()
    print('-----------------------------------')
    print_document_by_id("625e6ad796fbe33ab57144aa")
    print_document_by_id("625e6ad796fbe33ab57144ac")
    print('-----------------------------------')
    print_document_by_id_without_fields("625e6ad796fbe33ab57144aa")
    print_document_by_id_without_fields("625e6ad796fbe33ab57144ac")
    print('-----------------------------------')
    print_document_by_gt(29)
    print('-----------------------------------')
    print_documents_by_multiple_conditions()
    print('-----------------------------------')
    increase_age("625e6ad796fbe33ab57144ab")