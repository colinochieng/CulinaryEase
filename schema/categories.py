#!/usr/bin/python3
# to Be incorporated in letter times
"""
Define the Category class
Adding a Categories Table allows to organize
recipes into different types, making it easier
for users to find recipes based on their preferences 
"""
from sqlalchemy import Column, Integer, String, DateTime
from schema.recipe import Base
from sqlalchemy import ForeignKey, Text
from datetime import datetime


class Category(Base):
    """
    Define the structure of recipe categories
    """
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    image_url = Column(String(256), nullable=True)


class RecipeCategory(Base):
    """
    Define the many-to-many relationship between recipes and categories
    """
    __tablename__ = 'recipe_categories'
    recipe_id = Column(Integer, ForeignKey('recipes.id', ondelete='CASCADE'), primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.category_id', ondelete='CASCADE'), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
