from typing import Any
from flask import Blueprint, Response, request, jsonify


class InitRoute:
    def __init__(self) -> None:
        self.blueprint: Blueprint = Blueprint("helloworld", __name__)
        self.helloworld()
    
    def helloworld(self) -> None:
        @self.blueprint.route("/", methods=["GET"])
        def index() -> tuple[Any, int]:
            return jsonify({"message": "Hello World!"}), 200