from typing import Dict
import re
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create(self, person_info: Dict) -> Dict:
        first_name = person_info.get("first_name")
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_full_name(first_name=first_name, last_name=last_name)
        self.__insert_person_in_db(
            first_name=first_name,
            last_name=last_name,
            age=age,
            pet_id=pet_id)
        return self.__format_response(person_info)

    def __validate_full_name(self, first_name: str, last_name) -> None:
        # Regex para caracteres que não são letras
        invalid_characters = re.compile(r'[^a-z]', flags=re.IGNORECASE)

        if invalid_characters.search(
            first_name
            ) or invalid_characters.search(
                last_name):
            raise Exception("Nome da pessoa inválido!")

    def __insert_person_in_db(self,
                              first_name: str,
                              last_name: str,
                              age: int,
                              pet_id: int) -> None:
        self.__people_repository.insert_person(
            first_name=first_name,
            last_name=last_name,
            age=age,
            pet_id=pet_id)

    def __format_response(self, person: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person,
            }
        }
