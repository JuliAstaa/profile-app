from app.services.UserService import UserServices
from app import ProfileApp

class UserControllers:
    def __init__(self) -> None:
        self.session = ProfileApp().get_session

    def create_user(self, data):
        with self.session() as session:
            services = UserServices(session)
            try:
                new_user = services.create_users(data)
                return new_user.to_dict()
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