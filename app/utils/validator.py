from app.models.profile import Users

class Validator:
    @staticmethod
    def is_empty(data):
        if data is None or data == "":
            return True
        return False
    
    @staticmethod
    def is_email_taken(session, email, id=None):
        existing_email = session.query(Users).filter_by(email=email).first()
        if existing_email and existing_email.id != id:
            return True
        return False
    
    @staticmethod
    def is_username_taken(session, username, id=None):
        existing_username = session.query(Users).filter_by(username=username).first()
        if existing_username and existing_username.id != id:
            return True
        return False
    
    @staticmethod
    def user_validator(session, data):
        errors = {}

        if Validator.is_empty(data.get("username")):
            errors["username"] = "Username is required"
        if Validator.is_empty(data.get("email")):
            errors["email"] = "Email is required"
        if Validator.is_empty(data.get("password")):
            errors["password"] = "Password is required"
        if Validator.is_email_taken(session, data.get("email"), data.get("id")):
            errors["email"] = "Email already taken"
        if Validator.is_username_taken(session, data.get("username"), data.get("id")):
            errors["username"] = "Username already taken"

        return errors
    
    @staticmethod
    def login_validator(session, data):
        errors = {}

        if Validator.is_empty(data.get("username")):
            errors["username"] = "Username is required"
        if Validator.is_empty(data.get("password")):
            errors["password"] = "Password is required"

        return errors

        