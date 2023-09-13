#!/usr/bin/python3
"""
Module for Address Objects
"""
from schema.recipe import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String, Integer, Boolean
import uuid


class Address(Base):
    """
    A class representing user addresses in a database.

    Attributes:
        address_id (str): A unique identifier for the address.
        user_id (str): The user's identifier to whom the address belongs.
        city (str): The city of the address.
        state (str): The state or province of the address.
        country (str): The country of the address.

    Methods:
        __init__(): Initializes a new Address object with a unique ID.
        to_dict(): Converts the Address object to a dictionary for easy serialization.

    Note:
        This class represents the structure of the 'addresses' table in the database.
    """
    __tablename__ = 'addresses'
    address_id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'))
    city = Column(String(60))
    state = Column(String(60))
    country = Column(String(60))

    def __init__(self):
        self.address_id = str(uuid.uuid4())

    def to_dict(self):
        """
        Converts the Address object to a dictionary for easy serialization.

        Returns:
            dict: A dictionary representation of the Address object.
        """
        data = self.__dict__

        # Remove non-essential fields
        data.pop('_sa_instance_state', None)
        data.pop('user_id', None)

        return data
