#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from schema.recipe import Recipe, Base
from schema.users import User
from schema.ingredients import Ingredient, RecipeIngredient
from schema.likes import Likes
from schema.comments import Comments



class DataDriver:
    url = 'mysql+mysqldb://recipe:recipe_pwd@localhost/virtual_recipe_meal'
    
    def __init__(self):
        self.__driver = create_engine(self.url, pool_pre_ping=True)
        self.__session = None

    def restart(self):
        Base.metadata.create_all(self.__driver)
        Session = sessionmaker(bind=self.__driver, expire_on_commit=False)
        Scoped = scoped_session(session_factory=Session)
        self.__session = Scoped()
    

    def new(self, data):
        self.__session.add(data)
    
    def save(self):
        self.__session.commit()

    def get_user_by_email(self, email):
        return self.__session.query(User).filter(User.email == email).one_or_none()
    
    def get_user_by_uname(self, uname):
        return self.__session.query(User).filter_by(username=uname).one_or_none()
    
    def delete(self, user):
        """
        delete user account
        """
        self.__session.delete(user)

    def close(self):
        self.__session.close()

storage = DataDriver()
storage.restart()
