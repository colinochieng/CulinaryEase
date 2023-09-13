#!/usr/bin/python3
"""
Module for Comments Objects
"""
from schema.recipe import Base
from sqlalchemy import Column, Integer, ForeignKey, func, DateTime, orm
from sqlalchemy import Text, String
import uuid


class Comments(Base):
    """
    A class representing comments associated with recipes in a database.

    Attributes:
        comment_id (str): A unique identifier for the comment.
        user_id (str): The user's identifier who posted the comment.
        recipe_id (str): The identifier of the recipe to which the comment belongs.
        created_at (DateTime): The date and time when the comment was created.
        comment_text (str): The text of the comment.

    Relationships:
        User (relationship): Relationship to the User table, representing the user who posted the comment.

    Methods:
        __init__(): Initializes a new Comments object with a unique ID.

    Note:
        This class represents the structure of the 'comments' table in the database.
    """
    __tablename__ = 'comments'
    comment_id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'))
    recipe_id = Column(String(60), ForeignKey(
        'recipes.id', ondelete='CASCADE'))
    created_at = Column(DateTime, server_default=func.now())
    comment_text = Column(Text, nullable=False)

    # Define a relationship to the User table
    User = orm.relationship('User', backref='comments')

    def __init__(self):
        """
        Initializes a new Comments object with a unique ID.
        """
        self.comment_id = str(uuid.uuid4())
