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
from datetime import datetime
from schema.database.data_storage import storage
from flask import request, abort, jsonify, make_response, render_template
import re
from schema.recipe import Recipe
from schema.users import User


recipe_utils = {'title': 'required',
                'description': 'required',
                'instructions': 'required',
                'cuisine': 'required',
                'prep_time': 'required',
                'cook_time': 'required',
                'servings': 'required',
                'currency': 'required',
                'total_cost': 'required',
                'prep_time': 'required',}
recipe_optionals = {'video_link': 'optional',
                    'total_time': 'optional',
                    'calories': 'optional',
                    'nutrition': 'optional',
                    'notes': 'optional'
                    }
user_utils = {'username': 'required', 'password': 'required'}
