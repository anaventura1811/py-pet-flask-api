from typing import Dict
from .person_creator_view import PersonCreatorView
from .http_types.http_request import HttpRequest


class MockPersonCreatorController:
    def create(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }


def test_person_creator_view():

    body = {
        "first_name": "Ana",
        "last_name": "Ventura",
        "age": 33,
        "pet_id": 123,
    }

    http_request = HttpRequest(body=body)

    expected_response = {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": body
        }
    }

    controller = MockPersonCreatorController()
    view = PersonCreatorView(controller)
    response = view.handle(http_request)
    assert response is not None
    assert response.status_code == 201
    assert "data" in response.body
    assert "type" in response.body["data"]
    assert "count" in response.body["data"]
    assert response.body == expected_response
