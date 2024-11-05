import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository


db_connection_handler.connect_to_db()


# Teste de integração
@pytest.mark.skip(reason="integration test")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    repo.list_pets()
    # print(f"\n{response}")


@pytest.mark.skip(reason="integration test")
def test_delete_pet():
    repo = PetsRepository(db_connection_handler)
    repo.delete_pet(name="belinha")


@pytest.mark.skip(reason="integration test")
def test_insert_person():
    first_name = "Ana teste"
    last_name = "Last teste"
    age = 33
    pet_id = 8
    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(
        first_name=first_name,
        last_name=last_name,
        age=age,
        pet_id=pet_id)


@pytest.mark.skip(reason="integration test")
def test_get_person():
    person_id = 1
    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id=person_id)
    assert response is not None
