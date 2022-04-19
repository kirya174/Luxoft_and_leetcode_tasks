import pymongo
from pymongo import MongoClient
import config


def save_document(doc):
    with MongoClient(config.mongodb) as client:
        db = client[config.database]
        entities = db.entities
        result = entities.insert_one(doc.__dict__)
        return result


def save_documents(*docs):
    with MongoClient(config.mongodb) as client:
        db = client[config.database]
        entities = db.entities
        result = entities.insert_many([doc.__dict__ for doc in docs])
        return result


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


# peter = Person("Peter I", "Romanov", 30)
# save_document(peter)
# print("Complete")

person1 = Person("Ivan", "Ivanov", 43)
person2 = Person("Vasya", "Dedov", 20)
person3 = Person("Lenin", "LiveLikeLenin", 200)

ids = save_documents(person1, person2, person3)
print(ids.inserted_ids)
