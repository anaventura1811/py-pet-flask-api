from src.views.http_types.http_response import HttpResponse
from .error_types.http_bad_request import HttpBadRequestError
from .error_types.http_not_found import HttpNotFoundError
from .error_types.http_unprocessable_entity import HttpUnprocessableEntity


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpUnprocessableEntity,
                          HttpBadRequestError,
                          HttpNotFoundError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "message": error.message
                }]
            }
        )
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "ServerError",
                "message": str(error)
            }]
        }
    )
