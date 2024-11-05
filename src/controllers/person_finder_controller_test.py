# pylint: disable=too-many-arguments

from .person_finder_controller import PersonFinderController


class MockPerson:
    def __init__(self,
                 first_name, last_name, pet_name, pet_type, person_id) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.id = person_id


class MockPeopleRepository:
    def get_person(self, person_id: int):

        return MockPerson(
            first_name="Ana",
            last_name="Ventura",
            pet_name="Serena",
            pet_type="dog",
            person_id=person_id
        )


def test_find():
    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(123)
    expected_response = {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": "Ana",
                "last_name": "Ventura",
                "pet_name": "Serena",
                "pet_type": "dog"
            }
        }
    }
    assert "data" in response
    assert response == expected_response
