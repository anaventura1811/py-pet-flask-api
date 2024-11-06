from src.models.sqlite.entities.pets import PetsTable
from .pet_list_controller import PetListController


class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Serena", type="dog", id=10),
            PetsTable(name="Bentinho", type="cat", id=11)]


def test_list_pets():
    controller = PetListController(MockPetsRepository())
    response = controller.list()

    expected_response = {
       "data": {
           "type": "Pet",
           "count": 2,
           "attributes": [
               {"name": "Serena", "id": 10, "type": "dog"},
               {"name": "Bentinho", "id": 11, "type": "cat"}
           ]
       }
    }

    assert "data" in response
    assert response == expected_response
