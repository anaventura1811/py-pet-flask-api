import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository


db_connection_handler.connect_to_db()


# Teste de integração
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(f"\n{response}")


@pytest.mark.skip(reason="integration test")
def test_delete_pet():
    repo = PetsRepository(db_connection_handler)
    repo.delete_pet(name="belinha")
