#!/usr/bin/python3
"""
Database management engine file
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from schema.recipe import Recipe, Base
from schema.users import User
from schema.ingredients import Ingredient, RecipeIngredient
from schema.likes import Likes
from schema.comments import Comments


class DataDriver:
    """
    A class for managing data storage and database operations.

    Attributes:
        url (str): The URL for connecting to the database.

    Methods:
        __init__(): Initializes a DataDriver object with a database connection.
        restart(): Sets up the database schema and creates a new session.
        new(data): Adds a new data object to the session.
        save(): Commits changes to the database.
        get_user_by_email(email): Retrieves a user by their email address.
        get_user_by_uname(uname): Retrieves a user by their username.
        delete(user): Deletes a user account.
        close(): Closes the database session.

    Note:
        This class is designed to interact with a MySQL database using SQLAlchemy.
    """
    url = 'mysql+mysqldb://recipe:recipe_pwd@localhost/virtual_recipe_meal'

    def __init__(self):
        """
        Initializes a DataDriver object with a database connection.
        """
        self.__driver = create_engine(self.url, pool_pre_ping=True)
        self.__session = None

    def restart(self):
        """
        Sets up the database schema and creates a new session.
        """
        Base.metadata.create_all(self.__driver)
        Session = sessionmaker(bind=self.__driver, expire_on_commit=False)
        Scoped = scoped_session(session_factory=Session)
        self.__session = Scoped()

    def new(self, data):
        """
        Adds a new data object to the session.

        Args:
            data: The data object to be added to the session.
        """
        self.__session.add(data)

    def save(self):
        """
        Commits changes to the database.
        """
        self.__session.commit()

    def get_user_by_email(self, email):
        """
        Retrieves a user by their email address.

        Args:
            email (str): The email address of the user to be retrieved.

        Returns:
            User or None: The User object if found, or None if not found.
        """
        return self.__session.query(User).filter(User.email == email).one_or_none()

    def get_user_by_uname(self, uname):
        """
        Retrieves a user by their username.

        Args:
            uname (str): The username of the user to be retrieved.

        Returns:
            User or None: The User object if found, or None if not found.
        """
        return self.__session.query(User).filter_by(username=uname).one_or_none()

    def delete(self, user):
        """
        Deletes a user account.

        Args:
            user: The User object representing the user account to be deleted.
        """
        self.__session.delete(user)

    def close(self):
        """
        Closes the database session.
        """
        self.__session.close()


# Create an instance of the DataDriver class for data storage and database operations
storage = DataDriver()
storage.restart()  # Initialize and set up the database session.
