from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository


db_connection_handler.connect_to_db()


# Teste de integração
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(f"\n{response}")


def test_delete_test():
    repo = PetsRepository(db_connection_handler)
    repo.delete_pet(name="belinha")
    # print(f"\n{response}")
