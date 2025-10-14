from app.models.profile import Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import datetime, timedelta, timezone
import time

class UserServices:
    def __init__(self, session):
        self.session = session

    def create_users(self, data):
        data["password"] = generate_password_hash(data["password"], salt_length=16)
        try:
            new_user = Users(**data)
            self.session.add(new_user)
            self.session.commit()
            return new_user
        except Exception as e:
            self.session.rollback()
            raise {"message": str(e)}
    
    def login(self, data):
        now = time.time()
        try:
            user = self.session.query(Users).filter_by(username=data["username"]).first()
            if not user:
                return None
            
            if check_password_hash(user.password, data["password"]):
                access_token = create_access_token(identity=str(user.id), additional_claims={
                    "username": user.username,
                    "email": user.email
                },
                expires_delta=timedelta(minutes=30))

                refresh_token = create_refresh_token(identity=str(user.id), expires_delta=timedelta(days=7))

                return {
                    "tokens": {
                        "access": {
                            "token": access_token,
                            "expires_in": int(now + timedelta(minutes=30).total_seconds())
                        },
                        "refresh": {
                            "token": refresh_token,
                            "expires_in": int(now + timedelta(days=7).total_seconds())
                        }
                    },
                    "user": user.to_dict(),

                }
            else:
                return None
        except Exception as e:
            self.session.rollback()
            raise e

    def get_user(self, id):
        try:
            user = self.session.query(Users).filter_by(id=id).first()
            return user
        except Exception as e:
            self.session.rollback()
            raise e
