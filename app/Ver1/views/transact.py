#!/usr/bin/python3
"""
Module dealing with sessions management, authentication
creations of new recipe and accompaniments
"""
import json
from flask import jsonify, make_response
from app.Ver1.views import scheme
from schema.ingredients import Ingredient, RecipeIngredient
from flask import render_template, request, redirect, session
import requests
from schema.recipe import Recipe
from schema.database.data_storage import storage
from schema.users import User


@scheme.route('/status')
def status():
    """
    Check the status of the scheme.

    Returns:
        json: A JSON response indicating the status as 'ok'.
    """
    return jsonify({'Status': 'ok'})

@scheme.route('/login', methods=["GET", "POST"])
def login():
    """
    Handle user login.

    Returns:
        str: HTML content for the login page or a login confirmation message.
    """
    from flask import render_template_string
    if request.method == 'GET':
        return redirect('/', 302)

    email = request.form.get("email").lower()
    get_user = storage.get_user_by_email(email)
    print(get_user.id)
    
    session['user_id'] = get_user.id
    
    return render_template_string("""
<h1> Login </h1>
""")

@scheme.route("/logout")
def logout():
    """
    Handle user logout.

    Returns:
        response: A redirection response to the home page.
    """
    session.pop('user_id', None)
    return make_response(redirect('/', 302))


@scheme.route('/new_recipe')
def new_recipe():
    response, data, country = ('', '', '')
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        country = data["country"]
    except requests.exceptions.ConnectionError:
        pass

    state = None
    
    with open('app/Ver1/static/JS/states.json', 'r', encoding='utf-8') as file:
        states = json.load(file)
        state = states.get(country, None)
    
    if not state:
        with open('app/Ver1/static/JS/territories.json', 'r', encoding='utf-8') as file:
            territories = json.load(file)
            state = territories.get(country, None)
    
    if state:
        return render_template('recipe.html', states_name=state)
    else:
        if country:
            return render_template('recipe.html', states_name=country)
        else:
            return render_template('recipe.html', states_name='Korea')
    

@scheme.route('/submit_recipe', methods=['GET', 'POST'])
def submit_new_recipe():
    """
    Handle incoming recipe form and serve it to the database.

    Returns:
        json or str: A JSON response containing recipe data or an HTML response.
    """
    name = True
    if name:
        return request.form
    if request.method == 'POST':

        #  Check if user is logged in

        if not session.get('user_id'):
            return render_template('recipe.html', not_logged_in=True)

        amounts = []
        costs = []
        ingredient_names = []
        units = []

        archive = {}

        for key, value in request.form.items():
            if key.startswith('amount'):
                amounts.append(value)
            elif key.startswith('cost'):
                costs.append(value)
            elif key.startswith('ingredient_name'):
                ingredient_names.append(value)
            elif key.startswith('unit'):
                units.append(value)
            else:
                archive.update({key: value})

         # Create a new Recipe instance
        new_recipe_instance = Recipe()
        new_user = User()
        
        # Set the user_id of the new recipe to the user's ID
        new_recipe_instance.user_id = new_user.id

        # Set attributes of the new recipe based on form data
        for key, value in archive.items():
            new_recipe_instance.__setattr__(key, value)

        # Create Ingredient and RecipeIngredient instances for each ingredient

        for name, unit, quantity, cost in zip(ingredient_names, units, amounts, costs):
            new_ingredient = Ingredient()
            new_ingredient.__setattr__('name', name)
            new_ingredient.__setattr__('unit', unit)

            archive[name] = new_ingredient.ingredient_id

            new_recipe_ingredient = RecipeIngredient()
            new_recipe_ingredient.recipe = new_recipe_instance
            new_recipe_ingredient.ingredient = new_ingredient
            new_recipe_ingredient.quantity = quantity
            new_recipe_ingredient.cost = cost

            storage.new(new_recipe_ingredient)

        # Save changes to the database
        storage.save()

        return archive
    

@scheme.route("/recipe/123")
def display_recipe():
    """
    Display a specific recipe with ID 123.

    Returns:
        str: HTML content for displaying the recipe.
    """
    return render_template('display.html')

@scheme.route('/portfolio')
def portfolio():
    """
    Display a portfolio page.

    Returns:
        str: HTML content for displaying the portfolio.
    """
    return render_template('index.html')
