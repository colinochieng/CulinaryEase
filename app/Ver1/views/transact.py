from app.Ver1.views import scheme
from flask import render_template, request
from flask import jsonify
import json
import requests
from schema.ingredients import Ingredient, RecipeIngredient
from schema.recipe import Recipe
from schema.database.data_storage import storage
from schema.users import User


@scheme.route('/status')
def status():
    return jsonify({'Status': 'ok'})

@scheme.route('/login')
def login():
    return render_template('login.html')


@scheme.route('/new_recipe')
def new_recipe():
    response = requests.get('https://ipinfo.io/json')
    data = response.json()
    country = data["country"]
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
        return render_template('recipe.html', states_name=country)
    

@scheme.route('/submit_recipe', methods=['GET', 'POST'])
def submit_new_recipe():
    """
    handles incoming recipe form and serves it to the database
    """
    if request.method == 'POST':
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
        
        new_recipe_instance = Recipe()
        new_user = User()
        new_user.username = 'Colin'
        new_user.email = 'colin@okumu'
        new_user.set_passwd('Colin')

        new_recipe_instance.user_id = new_user.id
        storage.new(new_user)

        for key, value in archive.items():
            new_recipe_instance.__setattr__(key, value)

        archive.update({'newRecipe': new_recipe_instance.id})
        archive.update({'User': new_user.id})
        archive.update({'amounts': amounts})
        archive.update({'costs': costs})
        archive.update({'ingredient_names': ingredient_names})
        archive.update({'units': units})

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
        
        storage.save()

        return archive

@scheme.route('/portfolio')
def portfolio():
    return render_template('index.html')
