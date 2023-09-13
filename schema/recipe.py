#!/usr/bin/python3
"""
Define the Recipe class and its associated database structure.
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import ForeignKey, Text, func, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

# Create a base class for declarative ORM classes
Base = declarative_base()


class Recipe(Base):
    """
    A class representing a recipe in a database.

    Attributes:
        id (str): A unique identifier for the recipe.
        user_id (str): The user's identifier who created the recipe.
        title (str): The title of the recipe.
        description (str): A description of the recipe.
        instructions (str): Detailed cooking instructions.
        video_link (str): A link to a video demonstration of the recipe (nullable).
        created_at (DateTime): The date and time when the recipe was created.
        modified_at (DateTime): The date and time when the recipe was last modified.
        cuisine (str): The type of cuisine the recipe belongs to.
        prep_time (int): The preparation time in minutes.
        cook_time (int): The cooking time in minutes.
        total_time (int): The total time in minutes (prep_time + cook_time).
        servings (int): The number of servings the recipe yields.
        category (str): The category of the recipe (e.g., dessert, brunch).
        calories (int): The number of calories in the recipe (nullable).
        nutrition (str): Nutritional information for the recipe (nullable).
        likes (relationship): Relationship to the Likes table.
        comments (relationship): Relationship to the Comments table.
        notes (str): Additional notes or tips for the recipe (nullable).
        currency (str): The currency used for cost calculations.
        total_cost (Numeric): The total cost of ingredients for the recipe.
        recipe_profile_path (str): Path to a profile image for the recipe (nullable).
        recipe_ingredients (relationship): Relationship to the RecipeIngredient table.

    Methods:
        __init__(): Initializes a new Recipe object with a unique ID.

    Note:
        This class represents the structure of the 'recipes' table in the database.
    """
    # Specify the table name
    __tablename__ = 'recipes'

    # Define table columns
    id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String(256), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)
    video_link = Column(String(256), nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    modified_at = Column(DateTime, default=datetime.utcnow(),
                         nullable=False, onupdate=datetime.utcnow())
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
    recipe_profile_path = Column(String(256), nullable=True)
    recipe_ingredients = relationship(
        "RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan")
    # ingredients = relationship(
    #     'Ingredient',
    #     secondary='recipe_ingredients',
    #     back_populates='recipes')

    def __init__(self):
        self.id = str(uuid.uuid4())
