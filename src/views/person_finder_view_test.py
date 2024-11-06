from typing import Dict
from .person_finder_view import PersonFinderView
from .http_types.http_request import HttpRequest


class MockPersonFinderController:
    def __init__(self, person_info: Dict, person_id: int) -> None:
        self.__person_info = person_info
        self.__person_id = person_id

    def find(self, person_id: int) -> Dict:
        if person_id == self.__person_id:
            return {
                "data": {
                    "type": "Person",
                    "count": 1,
                    "attributes": self.__person_info
                }
            }
        return {}


def test_person_finder_view():

    param = {
        "person_id": 1
    }

    person_info = {
        "first_name": "Ana",
        "last_name": "Ventura",
        "pet_name": "Serena",
        "pet_type": "dog"
    }

    http_request = HttpRequest(param=param)

    expected_response = {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": person_info
        }
    }

    controller = MockPersonFinderController(person_id=param["person_id"], person_info=person_info)
    view = PersonFinderView(controller)
    response = view.handle(http_request)
    assert response is not None
    assert response.status_code == 200
    assert "data" in response.body
    assert "type" in response.body["data"]
    assert "count" in response.body["data"]
    assert response.body == expected_response
