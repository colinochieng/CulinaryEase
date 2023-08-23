#!/usr/bin/python3
"""
Module for Likes Objects
"""
import uuid
from schema.recipe import Base
from sqlalchemy import Column, Integer, ForeignKey, func, DateTime, orm, String


class Likes(Base):
    """
    Define likes for recipe
    """
    __tablename__ = 'likes'
    like_id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'))
    recipe_id = Column(String(60), ForeignKey('recipes.id', ondelete='CASCADE'))
    created_at = Column(DateTime, server_default=func.now())
    User = orm.relationship('User', backref='likes')

    def __init__(self):
        self.like_id = str(uuid.uuid4())
