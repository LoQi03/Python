from fastapi import FastAPI
from uvicorn import run
from src.repositories.person_repository import PersonRepository
from src.services.person_service import PersonService
from src.api.persons_api import init_persons_api
from pymongo import MongoClient


database_client = MongoClient("mongodb://localhost:27017/")

database = database_client["example"]


class Repositories:
    def __init__(self, database):
        self.person_repository = PersonRepository(database)

repositories = Repositories(database)

class Services:
    def __init__(self):
        self.person_service = PersonService(repositories.person_repository)

services = Services()

app = FastAPI()
init_persons_api(app, services)

if __name__ == "__main__":
    run("main:app", port=8000, reload=True)