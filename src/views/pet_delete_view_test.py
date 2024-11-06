from .pet_delete_view import PetDeleteView
from .http_types.http_request import HttpRequest


class MockPetDeleteController:
    def delete(self, name: str) -> None:
        pass


def test_pet_delete_view():

    param = {
        "name": "Bentinho"
    }

    http_request = HttpRequest(param=param)

    controller = MockPetDeleteController()
    view = PetDeleteView(controller)
    response = view.handle(http_request)
    assert response.status_code == 204
