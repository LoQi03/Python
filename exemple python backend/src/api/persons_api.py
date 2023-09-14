import json
import sys
sys.path.append('')
from src.models.person import Person
from bson import json_util

def init_persons_api(app, services):
    
    @app.post("/persons")
    async def add_person(name: str, age: int):
        person = Person(name, age)
        result = await services.person_service.add_person(person)
        return result
    
    @app.get("/persons")
    def get_all_persons():
        result =  services.person_service.get_all_persons()
        return json.loads(json_util.dumps(result))

    @app.delete("/persons/{id}")
    def delete_person(id: str):
        services.person_service.delete_person(id)
        return "Person deleted"
    
    @app.put("/persons/{id}")
    def update_person(id: str, name: str, age: int):
        person = Person(name, age)
        services.person_service.update_person(id, person)
        return "Person updated"
    
    @app.get("/persons/{id}")
    def get_person_by_id(id: str):
        result = services.person_service.get_person_by_id(id)
        return json.loads(json_util.dumps(result))
