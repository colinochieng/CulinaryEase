#!/usr/bin/python3
"""
Module for creation, deletion and update of recipe
Requires User's:
    -> username/email: for user id
    -> password: for account authentications
Requires recipe's:
    -> full data for creation of new instances
    -> 
"""
from schema.address import Address
from app.Ver1.api import blueprint
from schema.ingredients import Ingredient, RecipeIngredient
from datetime import datetime
from schema.database.data_storage import storage
from flask import request, abort, jsonify, make_response, render_template
import re
from schema.recipe import Recipe
from schema.users import User


recipe_create_utils = {'title': 'required',
                'user': {'username': 'required', 'password': 'required'},
                'description': 'required',
                'instructions': 'required',
                'cuisine': 'required',
                'prep_time': 'required',
                'cook_time': 'required',
                'servings': 'required',
                'currency': 'required',
                'total_cost': 'required',
                'prep_time': 'required',
                'ingredients': {'ingre1': {"name": 'required', 'unitOfMeasure': 'required',
                                           'cost': 'required', 'quantity': 'required', },
                                'ingre2': {"name": 'required', 'unitOfMeasure': 'required',
                                           'cost': 'required', 'quantity': 'required', }}}

recipe_create_options = {'video_link': 'optional',
                'total_time': 'optional',
                'calories': 'optional',
                'nutrition': 'optional',
                'notes': 'optional'}


@blueprint.route('/recipes/create', methods=['POST'])
def create_recipe():
    """
    creates new recipe raw
    """
    if request.is_json:
        info_required = [key for key in recipe_create_utils if key not in request.json]

        if info_required.__len__() > 0:
            return jsonify({'message': f'missing => {info_required}', 'note': recipe_create_utils | recipe_create_options,
                            'status': 'fail'}), 200
        
        
        
        else:
            return jsonify({"hello": 'world'}), 200
    else:
        return jsonify({'message': 'Only Json is Required', 'status': 'fail'}), 200