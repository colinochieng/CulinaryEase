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
    Define Comments for recipe/
    """
    __tablename__  = 'comments'
    comment_id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'))
    recipe_id = Column(String(60), ForeignKey('recipes.id', ondelete='CASCADE'))
    created_at = Column(DateTime, server_default=func.now())
    comment_text = Column(Text, nullable=False)
    User = orm.relationship('User', backref='comments')

    def __init__(self):
        self.comment_id = str(uuid.uuid4())
