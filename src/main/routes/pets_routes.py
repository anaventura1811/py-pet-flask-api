from flask import Blueprint, jsonify
from src.main.composer.pet_list_composer import pet_list_composer
from src.main.composer.pet_delete_composer import pet_delete_composer
from src.views.http_types.http_request import HttpRequest
from src.errors.error_handler import handle_errors


pets_routes_bp = Blueprint("pets_routes", __name__)


@pets_routes_bp.route('/pets', methods=["GET"])
def list_pets():
    try:
        http_request = HttpRequest()
        view = pet_list_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code

    except Exception as exc:
        http_response = handle_errors(exc)
        return jsonify(http_response.body), http_response.status_code


@pets_routes_bp.route('/pets/<name>', methods=["DELETE"])
def delete_pet(name: str):
    try:

        http_request = HttpRequest(param={"name": name})
        view = pet_delete_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code

    except Exception as excep:
        http_response = handle_errors(excep)
        return jsonify(http_response.body), http_response.status_code
