from app.services.UserService import UserServices
from app import ProfileApp
from app.utils.validator import Validator

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
                    return user.to_dict()
                else:
                    return {"errors": errors}
            except RuntimeError as e:
                return {"message": str(e)}

    def login(self, data):
        with self.session() as session:
            services = UserServices(session)
            try:
                user = services.login(data)
                return user
            except RuntimeError as e:
                return {"message": str(e)}
    
    def get_user(self, id):
        with self.session() as session:
            services = UserServices(session)
            try:
                user = services.get_user(id)
                return user.to_dict()
            except RuntimeError as e:
                return {"message": str(e)}