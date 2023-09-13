#!/usr/bin/python3
"""
Module Noting the requirements for the user to login
"""
from schema.recipe import Base
import bcrypt
from sqlalchemy import Column, String
from sqlalchemy import Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

# Constant pepper for password security
PEPPER = b'culinarysuperpepper'


class User(Base):
    """
    Class for defining the platforms users
    Attributes:
        id (UUID String):= unique user id
        username (string):= unique user's choosen username
        email (string):= users email, unique
        password_hash (string):= bcrypted passwords
        created_at (Datetime):= time of creation of user account
        updated_at (Datetime):= time of update of user account
        profile_picture(string):= path to the profile picture of user
        bios(string):= users bios
        recipes(orm-relationship-obj):= link to creation of one to many relationships
            with the recipes table
        addresses(orm-relationship-obj):= link to creation of one to many relationships
            with the addresses table
    """
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True)
    username = Column(String(60), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password_hash = Column(String(60), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    profile_picture = Column(String(120), nullable=False,
                             default='profile_picture.png')
    bios = Column(Text, nullable=True)
    recipes = relationship('Recipe', backref='artist')
    addresses = relationship('Address', backref='user')

    def __init__(self):
        """
        Intializes new user, generates a unique id for the user
        Args:
            self(user):=new user object
        """
        self.id = str(uuid.uuid4())

    def set_passwd(self, password):
        """
        Hash the password
        Args:
            self(user):=new user object
            password(string): user entered passcode
        Returns:
            None
        """
        salt = bcrypt.gensalt()
        hashed_pwd = bcrypt.hashpw(PEPPER + password.encode('utf-8'), salt)
        self.password_hash = hashed_pwd.decode('utf-8')

    def check_password(self, password):
        """
        Check if the provided password matches the stored password hash.
        Args:
            password (str):= The password to be checked.
        Returns:
            bool: True if the provided password matches the stored hash,
                False otherwise.
        """
        return bcrypt.checkpw(PEPPER + password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def to_dict(self):
        """
        Convert the user object to a dictionary representation.
        Returns:
            dict: A dictionary containing user data
            with certain fields removed or modified.
        """
        data = self.__dict__

        # Remove sensitive information
        data.pop('password_hash', None)

        # Conditionally remove or modify fields
        if len(self.recipes) > 0:
            pass
        else:
            del data['recipes']
        if len(self.addresses) > 0:
            data.update({'addresses': data['addresses'][0].to_dict()})
        else:
            del data['addresses']
        # Remove internal attributes
        data.pop('_sa_instance_state', None)
        data.pop('profile_picture', None)
        data.pop('created_at', None)
        data.pop('updated_at', None)

        return data
