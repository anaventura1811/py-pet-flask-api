from typing import Dict
from .pet_delete_view import PetDeleteView


class MockHttpRequest:
    def __init__(self, param: Dict = None) -> None:
        self.param = param

class MockPetDeleteController:
    def delete(self, name: str) -> None:
        pass


def test_pet_delete_view():

    param = {
        "name": "Bentinho"
    }

    http_request = MockHttpRequest(param=param)

    controller = MockPetDeleteController()
    view = PetDeleteView(controller)
    response = view.handle(http_request)
    assert response.status_code == 204
