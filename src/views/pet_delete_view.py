from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.pet_delete_controller import PetDeleteControllerInterface
from .interfaces.view_interface import ViewInterface


class PetDeleteView(ViewInterface):
    def __init__(self, controller: PetDeleteControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.param["name"]
        self.__controller.delete(name=name)
        return HttpResponse(status_code=204)