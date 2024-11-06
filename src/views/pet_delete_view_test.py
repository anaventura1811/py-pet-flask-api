from .pet_delete_view import PetDeleteView
from .mock_http_request import MockHttpRequest


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
