import config
from pymongo import MongoClient
from mongo_search import print_all


def remove_document_by_gt_age(age):
    condition_query = {"age": {"$gt": age}}
    with MongoClient(config.mongodb) as client:
        db = client[config.database]
        entities = db.entities
        entities.delete_many(condition_query)


remove_document_by_gt_age(42)
print_all()