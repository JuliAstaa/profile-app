import os
from typing import Callable
from flask_jwt_extended import JWTManager
from flask import Flask
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.models.profile import Base

load_dotenv()

class ProfileApp:
    def __init__(self) -> None:
        self.app: Flask = Flask(__name__)
        self.abs_path: str = os.path.dirname(os.path.abspath(__file__))
        self.config()
        self.init_db()
        self.get_session()
        self.jwt()
        

    def config(self) -> None:
        self.app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(self.abs_path, 'profile.db')}"
        self.app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    
    def router(self) -> None:
        from app.routes.helloworldRouter import InitRoute
        from app.routes.UserRouter import UserRouters
        from app.routes.ProfileRouter import ProfileRouter
        self.app.register_blueprint(InitRoute().blueprint)
        self.app.register_blueprint(UserRouters().blueprint)
        self.app.register_blueprint(ProfileRouter().blueprint)

    def init_db(self) -> None:
        database_uri = f"sqlite:///{os.path.join(self.abs_path, 'profile.db')}"
        self.engine = create_engine(database_uri, echo=True)
        self.SessionLocal = sessionmaker(bind=self.engine, future=True, autoflush=True)
        Base.metadata.create_all(self.engine)
        
    def get_session(self):
        return self.SessionLocal()
    
    def jwt(self):
        self.jwt = JWTManager(self.app)

    def run(self) -> None:
        self.router()
        self.app.run(debug=True)