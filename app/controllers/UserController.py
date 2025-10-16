from app.services.UserService import UserServices
from app import ProfileApp
from app.utils.validator import Validator
from app.utils.response import Response

class UserControllers:
    def __init__(self) -> None:
        self.session = ProfileApp().get_session

    def create_user(self, data):
        with self.session() as session:
            services = UserServices(session)
            try:
                errors = Validator.user_validator(session, data)
                if errors == {}:
                    user = services.create_users(data)
                    return Response.success(200, "User created successfully", data=user.to_dict())
                else:
                    return Response.error(400, "User not created", errors=errors)
            except RuntimeError as e:
                return Response.error(400, "User not created", errors=e)

    def login(self, data):
        with self.session() as session:
            services = UserServices(session)
            try:
                errors = Validator.login_validator(session=session, data=data)

                if errors == {}:
                    user = services.login(data)
                    return Response.success(200, "User logged in successfully", data=user)
                else:
                    return Response.error(400, "User not logged in", errors=errors)
            except RuntimeError as e:
                return Response.error(400, "User not logged in", errors=e)
    
    def get_user(self, id):
        with self.session() as session:
            services = UserServices(session)
            try:
                user = services.get_user(id)
                if user:
                    return Response.success(200, "User fetched successfully", data=user.to_dict())
                else:
                    return Response.error(404, "User not found")
            except RuntimeError as e:
                return Response.error(400, "User not fetched", errors=e)