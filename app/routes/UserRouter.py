from flask import Blueprint, request, jsonify
from app.controllers.UserController import UserControllers
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.response import Response

class UserRouters:
    def __init__(self):
        self.blueprint = Blueprint("user", __name__)
        self.controllers = UserControllers()
        self.router_register()
        self.router_login()
        
    def router_register(self):
        @self.blueprint.route('/user/register', methods=["POST"])
        def register():
            if request.method == "POST":
                data = request.get_json()
                result = self.controllers.create_user(data)
                return result
            else:
                return jsonify(Response.response(405, "Method not allowed")), 405

    def router_login(self):
        @self.blueprint.route('/user/login', methods=["POST"])
        def login():
            if request.method == "POST":
                data = request.get_json()
                result = self.controllers.login(data)
                return result
            else:
                return {
                    "status": 405,
                    "message": "Method not allowed"
                }, 405
