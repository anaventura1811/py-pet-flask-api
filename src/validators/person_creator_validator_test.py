from .person_creator_validator import person_creator_validator

class MockRequest:
    def __init__(self, body) -> None:
        self.body = body


def test_person_creator_validator():
    request = MockRequest(body={
        "first_name": "Fulana",
        "last_name": "DeTal",
        "age": 30,
        "pet_id": 7,
    })
    person_creator_validator(request)


def test_person_creator_validator_error():
    request = MockRequest(body={
        "first_name": "Fulana",
        "last_name": "DeTal",
        "age": "30",
        "pet_id": 7,
    })
    person_creator_validator(request)
