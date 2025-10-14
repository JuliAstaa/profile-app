from flask import Blueprint, request
from app.controllers.UserController import UserControllers
from flask_jwt_extended import jwt_required, get_jwt_identity

class UserRouters:
    def __init__(self):
        self.blueprint = Blueprint("user", __name__)
        self.controllers = UserControllers()
        self.router_register()
        self.router_login()
        self.router_profile()
        
    def router_register(self):
        @self.blueprint.route('/user/add', methods=["POST"])
        def register():
            if request.method == "POST":
                data = request.get_json()
                result = self.controllers.create_user(data)
                return result
            else:
                return {
                    "status": 405,
                    "message": "Method not allowed"
                }, 405

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

    def router_profile(self):
        @self.blueprint.route('/user/profile', methods=["GET"])
        @jwt_required(optional=True, refresh=True)
        def profile():
            if request.method == "GET":
                id = get_jwt_identity()
                result = self.controllers.get_user(int(id))
                return result
            else:
                return {
                    "status": 405,
                    "message": "Method not allowed"
                }, 405