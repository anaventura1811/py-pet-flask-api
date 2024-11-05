from unittest import mock
# import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
# from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import PetsTable
from .people_repository import PeopleRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PeopleTable).one()],
                    [PeopleTable(
                        id=30,
                        first_name="Ana",
                        last_name="Ventura",
                        age=33,
                        pet_id=2)],
                ),
                (
                    [mock.call.filter(PeopleTable.id == 30)],
                    [PeopleTable(
                        id=30,
                        first_name="Ana",
                        last_name="Ventura",
                        age=33,
                        pet_id=2)]
                ),
                (
                    [mock.call.outerjoin(
                        PetsTable, PetsTable.id == PeopleTable.pet_id
                        )],
                    [PetsTable(
                        name="Serena",
                        type="dog"
                    )]
                ),
                ([mock.call.with_entities(
                    PeopleTable.first_name,
                    PeopleTable.last_name,
                    PetsTable.name.label("pet_name"),
                    PetsTable.type.label("pet_type"))],
                    ("Ana", "Ventura", "Serena", "dog")),
                (
                    # [mock.call.query(PeopleTable).one()],
                    # ("Ana", "Ventura", "Serena", "dog")
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# @pytest.mark.skip(reason="integration test")
def test_get_person():
    mock_connection = MockConnection()
    repo = PeopleRepository(mock_connection)
    person_id = 30
    res = repo.get_person(person_id)
    print(f"\n {res}")
    mock_connection.session.query.assert_called_once_with(PeopleTable)
    mock_connection.session.filter.assert_called_with(
        PeopleTable.id == person_id)
    mock_connection.session.outerjoin.assert_called_once()
