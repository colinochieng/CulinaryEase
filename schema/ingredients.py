#!/usr/bin/python3
"""
Define the Ingredients class
The Ingredients Table provides a centralized
repository for all ingredients used in recipes.
"""
from sqlalchemy import Column, Integer, String, DateTime
from schema.recipe import Base
from sqlalchemy import ForeignKey, func, orm, Table, Numeric, Float
import uuid


class Ingredient(Base):
    """
    Define the structure of ingredients
    """
    __tablename__ = 'ingredients'
    ingredient_id = Column(String(60), primary_key=True)
    name = Column(String(100), nullable=False)
    unit = Column(String(20), nullable=True)
    # image_url = Column(String(256), nullable=True)
    # recipes = orm.relationship(
    #     'Recipe',
    #     secondary='recipe_ingredients',
    #     back_populates='ingredients'
    # )
    recipe_ingredients = orm.relationship("RecipeIngredient", back_populates="ingredient", cascade="all, delete-orphan")

    def __init__(self):
        self.ingredient_id = uuid.uuid4()


class RecipeIngredient(Base):
    """
    Define the junction table for the relationship
    between Recipe and Ingredient
    with additional columns for amount and cost
    """
    __tablename__ = 'recipe_ingredients'
    recipe_id = Column(String(60), ForeignKey('recipes.id', ondelete='CASCADE'), primary_key=True)
    ingredient_id = Column(String(60), ForeignKey('ingredients.ingredient_id', ondelete='CASCADE'), primary_key=True)
    quantity = Column(Float, nullable=False)
    cost = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    #  Relationships
    recipe = orm.relationship("Recipe", back_populates="recipe_ingredients")
    ingredient = orm.relationship("Ingredient", back_populates="recipe_ingredients")



# Create a simple table object called recipe_ingredients
# recipe_ingredients = Table(
#     'recipe_ingredients',
#     Base.metadata,
#     Column('recipe_id', String(60), ForeignKey('recipes.id', ondelete='CASCADE'), primary_key=True),
#     Column('ingredient_id', String(60), ForeignKey('ingredients.ingredient_id', ondelete='CASCADE'), primary_key=True),
#     Column('quantity', String(50), nullable=False),
#     Column('created_at', DateTime, server_default=func.now())
# )
