from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)

    # relasi ke profile
    profile = relationship("Profile", back_populates="user", uselist=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }

class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    f_name = Column(String(50), nullable=False)
    l_name = Column(String(50))
    address = Column(String(100), nullable=False)
    phone_number = Column(String(15), nullable=False)
    pfp = Column(String(100), nullable=False)

    # foreign key 
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)

    # relasi ke users
    user = relationship("Users", back_populates="profile")