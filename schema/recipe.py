#!/usr/bin/python3
"""
Define the recipe class
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class Recipe(Base):
    """
    Define the structure of the recipe to execute
    """
    __tablename__ = 'Recipe'
    recipe_id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128), nullable=False)
    ingredients = Column('ingredients', String(256), nullable=False)
    preparation = Column('preparation', String(2000), nullable=False)
    category = Column('category', String(128), default='Fit for all')
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
