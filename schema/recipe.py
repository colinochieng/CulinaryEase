#!/usr/bin/python3
"""
Define the recipe class
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import ForeignKey, Text, func, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid


Base = declarative_base()


class Recipe(Base):
    """
    Define the structure of the recipe to execute
    """
    __tablename__ = 'recipes'
    id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String(256), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    # ingredients = relationship(
    #     'Ingredient',
    #     secondary='recipe_ingredients',
    #     back_populates='recipes')
    instructions = Column(Text, nullable=False)
    video_link = Column(String(256), nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    modified_at = Column(DateTime, default=datetime.utcnow(), nullable=False, onupdate=datetime.utcnow())
    cuisine = Column(String(60), nullable=False)
    prep_time = Column(Integer, nullable=False)
    cook_time = Column(Integer, nullable=False)
    total_time = Column(Integer, nullable=False)
    servings = Column(Integer, nullable=False)
    category = Column(String(128), default='All', nullable=False)
    calories = Column(Integer, nullable=True)
    nutrition = Column(Text, nullable=True)
    likes = relationship('Likes', backref='recipe')
    comments = relationship('Comments', backref='recipe')
    notes = Column(Text, nullable=True)
    currency = Column(String(128), nullable=False)
    total_cost = Column(Numeric(10, 2), nullable=False)
    recipe_ingredients = relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan")

    def __init__(self):
        self.id = str(uuid.uuid4())
