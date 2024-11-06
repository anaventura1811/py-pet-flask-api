from typing import List, Dict
from src.models.sqlite.entities.pets import PetsTable
from .pet_list_view import PetListView


class MockHttpRequest:
    def __init__(self) -> None:
        pass

class MockPetListController:
    def __init__(self, pets: List[PetsTable]) -> None:
        self.__pets = pets

    def list(self) -> Dict:
        pets_formatted = self.__format_response(self.__pets)
        return pets_formatted

    def __to_dict(self, pet: PetsTable) -> Dict:
        return {"name": pet.name, "type": pet.type}

    def __format_response(self, pets: List[PetsTable]) -> Dict:
        pets_formatted = [self.__to_dict(pet) for pet in pets]
        return {
            "data": {
                "type": "Pet",
                "count": len(pets_formatted),
                "attributes": pets_formatted
            }
        }


def test_pet_list_view():
    pets = [PetsTable(id=1, name="Serena", type="dog"),
            PetsTable(id=2, name="Bentinho", type="cat")]

    http_request = MockHttpRequest()

    expected_response = {
        "data": {
            "type": "Pet",
            "count": 2,
            "attributes": [{"name": "Serena", "type": "dog"}, {"name": "Bentinho", "type": "cat"}]
        }
    }

    controller = MockPetListController(pets=pets)
    view = PetListView(controller)
    response = view.handle(http_request)
    assert response is not None
    assert response.status_code == 200
    assert "data" in response.body
    assert "type" in response.body["data"]
    assert "count" in response.body["data"]
    assert response.body == expected_response
