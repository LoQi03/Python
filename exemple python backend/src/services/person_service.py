import sys
sys.path.append('src/')
from repositories.person_repository import PersonRepository
from models.person import Person

class PersonService:
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository
    
    async def add_person(self, person):
        result = await self.person_repository.add_person(person)
        return result
        
    def get_all_persons(self):
        result = self.person_repository.get_all_persons()
        return result
    
    def delete_person(self, id):
        self.person_repository.remove_person(id)

    def update_person(self, id, person):
        self.person_repository.update_person(id, person)
        
    def get_person_by_id(self, id):
        result = self.person_repository.get_person_by_id(id)
        return result