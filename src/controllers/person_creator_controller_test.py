import pytest
from .person_creator_controller import PersonCreatorController


class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass


def test_create():
    person_info = {
        "first_name": "Ana",
        "last_name": "Teste",
        "age": 33,
        "pet_id": 123,
    }

    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_info=person_info)
    assert "data" in response
    assert "type" in response["data"]
    assert "count" in response["data"]
    assert "attributes" in response["data"]
    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert "first_name" in response["data"]["attributes"]
    assert "last_name" in response["data"]["attributes"]
    assert "age" in response["data"]["attributes"]
    assert "pet_id" in response["data"]["attributes"]
    assert response["data"]["attributes"] == person_info


def test_create_error():
    person_info = {
        "first_name": "Ana123",
        "last_name": "Teste",
        "age": 33,
        "pet_id": 123,
    }

    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(Exception) as exceptinfo:
        controller.create(person_info=person_info)
        assert str(exceptinfo.value) == 'Nome da pessoa inválido!'
