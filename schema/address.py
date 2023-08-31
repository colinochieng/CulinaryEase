#!/usr/bin/python3
"""
Addresses
"""
from schema.recipe import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String, Integer, Boolean
import uuid


class Address(Base):
    """
    User Addresses
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
        Addresses dictionary
        """
        data = self.__dict__
        
        data.pop('_sa_instance_state', None)
        data.pop('user_id', None)

        return data
