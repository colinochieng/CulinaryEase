
from schema.recipe import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    """User Class"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(60), nullable=False)
    surname = Column(String(60), nullable=False)
    email = Column(String(128), nullable=True)
    password = Column(String(20), nullable=False)
    recipes = relationship('Recipe', backref='artist')

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "surname": self.surname,
            "email": self.email,}
