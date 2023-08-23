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
    street_address = Column(String(60))
    city = Column(String(60))
    state = Column(String(60))
    postal_code = Column(String(60))
    country = Column(String(60))
    is_default = Column(Boolean, default=False)

    def __init__(self):
        self.address_id = str(uuid.uuid4())
