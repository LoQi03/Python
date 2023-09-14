import sys
sys.path.append('src')
from models.person import Person
from bson.objectid import ObjectId

class PersonRepository:
    def __init__(self,database):
        self.persons_collection = database["persons"]
    
    def add_person(self, person :Person):
        person_dict = person.to_dict()
        result =  self.persons_collection.insert_one(person_dict)
        return result.inserted_id
    
    def get_all_persons(self):
        cursor =  self.persons_collection.find({})
        result = []
        for document in cursor:
            result.append(document)
        
        return result
    
    def remove_person(self, id):
        self.persons_collection.delete_one({"_id": ObjectId(id)})
        
    def update_person(self, id, person):
        person_dict = person.to_dict()
        self.persons_collection.update_one({"_id": ObjectId(id)}, {"$set": person_dict})
        
    def get_person_by_id(self, id):
        result = self.persons_collection.find_one({"_id": ObjectId(id)})
        return result