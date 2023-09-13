#!/usr/bin/python3
# to Be incorporated in letter times
"""
Module for Category Objects
"""
from sqlalchemy import Column, Integer, String, DateTime
from schema.recipe import Base
from sqlalchemy import ForeignKey, Text
from datetime import datetime


class Category(Base):
    """
    A class representing recipe categories in a database.

    Attributes:
        category_id (int): A unique identifier for the category (auto-incremented).
        name (str): The name of the category.
        description (str): A description of the category (nullable).
        image_url (str): A URL to an image associated with the category (nullable).

    Note:
        This class represents the structure of the 'categories' table in the database.
    """
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    image_url = Column(String(256), nullable=True)


class RecipeCategory(Base):
    """
    A class representing the many-to-many relationship between recipes and categories.

    Attributes:
        recipe_id (int): The identifier of the recipe.
        category_id (int): The identifier of the category.
        created_at (DateTime): The date and time when the relationship was created.

    Note:
        This class represents the structure of the 'recipe_categories' table in the database.
    """
    # Specify the table name
    __tablename__ = 'recipe_categories'
    recipe_id = Column(Integer, ForeignKey(
        'recipes.id', ondelete='CASCADE'), primary_key=True)
    category_id = Column(Integer, ForeignKey(
        'categories.category_id', ondelete='CASCADE'), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
