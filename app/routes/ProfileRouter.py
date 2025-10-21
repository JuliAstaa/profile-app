from flask import Blueprint, jsonify, request
from app.controllers.ProfileController import ProfileControllers
from flask_jwt_extended import jwt_required, get_jwt_identity

class ProfileRouter:
    def __init__(self):
        self.blueprint = Blueprint("profile", __name__)
        self.controllers = ProfileControllers()
        self.router_profile()
        self.create_profile_router()

    def router_profile(self):
        @self.blueprint.route('/profile', methods=["GET"])
        @jwt_required()
        def profile():
            if request.method == "GET":
                id = get_jwt_identity()
                result = self.controllers.get_profile_controller(int(id))
                return result
            else:
                return {
                    "status": 405,
                    "message": "Method not allowed"
                }, 405
    
    def create_profile_router(self):
        @self.blueprint.route('/profile/create', methods=["POST"])
        @jwt_required()
        def create_profile():
            if request.method == "POST":
                id = get_jwt_identity()
                data = request.get_json()
                result = self.controllers.create_profile_controller(id=id, data=data)
                return result
            else:
                return jsonify(Response.response(405, "Method not allowed")), 405
