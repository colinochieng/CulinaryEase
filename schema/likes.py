#!/usr/bin/python3
"""
Module for Likes Objects
"""
import uuid
from schema.recipe import Base
from sqlalchemy import Column, Integer, ForeignKey, func, DateTime, orm, String


class Likes(Base):
    """
    A class representing likes for recipes in a database.

    Attributes:
        like_id (str): A unique identifier for the like.
        user_id (str): The user's identifier who liked the recipe.
        recipe_id (str): The identifier of the recipe that was liked.
        created_at (DateTime): The date and time when the like was created.

    Relationships:
        User (relationship): Relationship to the User table, representing the user who liked the recipe.

    Methods:
        __init__(): Initializes a new Likes object with a unique ID.

    Note:
        This class represents the structure of the 'likes' table in the database.
    """

    # Specify the table name
    __tablename__ = 'likes'
    like_id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'))
    recipe_id = Column(String(60), ForeignKey(
        'recipes.id', ondelete='CASCADE'))
    created_at = Column(DateTime, server_default=func.now())

    # Define a relationship to the User table
    User = orm.relationship('User', backref='likes')

    def __init__(self):
        """
        Initializes a new Likes object with a unique ID.
        """
        self.like_id = str(uuid.uuid4())
