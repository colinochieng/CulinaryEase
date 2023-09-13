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
    A class representing ingredients in a database.

    Attributes:
        ingredient_id (str): A unique identifier for the ingredient.
        name (str): The name of the ingredient.
        unit (str): The unit of measurement for the ingredient (nullable).

    Relationships:
        recipe_ingredients (relationship): Relationship to the RecipeIngredient table.

    Methods:
        __init__(): Initializes a new Ingredient object with a unique ID.

    Note:
        This class represents the structure of the 'ingredients' table in the database.
    """
    __tablename__ = 'ingredients'
    ingredient_id = Column(String(60), primary_key=True)
    name = Column(String(100), nullable=False)
    unit = Column(String(20), nullable=True)

    # Define a relationship to the RecipeIngredient table
    recipe_ingredients = orm.relationship(
        "RecipeIngredient", back_populates="ingredient", cascade="all, delete-orphan")

    # image_url = Column(String(256), nullable=True)
    # recipes = orm.relationship(
    #     'Recipe',
    #     secondary='recipe_ingredients',
    #     back_populates='ingredients'
    # )

    def __init__(self):
        """
        Initializes a new Ingredient object with a unique ID.
        """
        self.ingredient_id = uuid.uuid4()


class RecipeIngredient(Base):
    """
    A class representing the junction table between recipes and ingredients
    with additional columns for quantity and cost.

    Attributes:
        recipe_id (str): The identifier of the recipe.
        ingredient_id (str): The identifier of the ingredient.
        quantity (float): The quantity of the ingredient required in the recipe.
        cost (Numeric): The cost of the ingredient in the recipe.
        created_at (DateTime): The date and time when the record was created.

    Relationships:
        recipe (relationship): Relationship to the Recipe table.
        ingredient (relationship): Relationship to the Ingredient table.

    Note:
        This class represents the structure of the 'recipe_ingredients' table in the database.
    """
    # Specify the table name
    __tablename__ = 'recipe_ingredients'
    recipe_id = Column(String(60), ForeignKey(
        'recipes.id', ondelete='CASCADE'), primary_key=True)
    ingredient_id = Column(String(60), ForeignKey(
        'ingredients.ingredient_id', ondelete='CASCADE'), primary_key=True)
    quantity = Column(Float, nullable=False)
    cost = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    # Define relationships to the Recipe and Ingredient tables
    recipe = orm.relationship("Recipe", back_populates="recipe_ingredients")
    ingredient = orm.relationship(
        "Ingredient", back_populates="recipe_ingredients")


# Create a simple table object called recipe_ingredients
# recipe_ingredients = Table(
#     'recipe_ingredients',
#     Base.metadata,
#     Column('recipe_id', String(60), ForeignKey('recipes.id', ondelete='CASCADE'), primary_key=True),
#     Column('ingredient_id', String(60), ForeignKey('ingredients.ingredient_id', ondelete='CASCADE'), primary_key=True),
#     Column('quantity', String(50), nullable=False),
#     Column('created_at', DateTime, server_default=func.now())
# )
