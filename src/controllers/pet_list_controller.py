from typing import Dict, List
import src.models.sqlite.interfaces.pets_repository as intf
from src.models.sqlite.entities.pets import PetsTable


class PetListController:
    def __init__(self, pet_repository: intf.PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    def __format_response(self, pets: List[PetsTable]) -> Dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append(
                {"name": pet.name, "id": pet.id, "type": pet.type})
        return {
            "data": {
                "type": "Pet",
                "count": len(formatted_pets),
                "attributes": formatted_pets
            }
        }
