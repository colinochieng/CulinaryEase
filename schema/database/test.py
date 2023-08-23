from schema.database.data_storage import storage
from schema.recipe import Recipe
from schema.users import User
from schema.ingredients import Ingredient, RecipeIngredient
from schema.likes import Likes
from schema.comments import Comments


user  = storage.get_user_by_email('colin@gmail.com')
print(user)
# # Create example user, category, and ingredients
# user = User()
# user.__setattr__('username', 'Joonwoo')
# user.__setattr__('email', 'colin@gmail.com')
# user.set_passwd('colin')
# storage.new(user)

# category = 'Dinner'

# recipe_data = {
#     'user_id': user.id,
#     'title': 'Delicious Grilled Chicken',
#     'description': 'A mouthwatering recipe for grilled chicken',
#     'instructions': '1. Marinate chicken with olive oil and salt. 2. Grill until cooked. 3. Enjoy!',
#     'category': category,
#     'cuisine': 'American',
#     'cook_time': 30,
#     'servings': 2,
#     'calories': 300,
#     'nutrition': 'High in protein and healthy fats'
# }

# # Create example recipe
# new_recipe = Recipe()
# for k, v in recipe_data.items():
#     new_recipe.__setattr__(k, v)

# ingredient1 = Ingredient()
# ingredient1.name = 'Chicken Breast'
# # ingredient2 = Ingredient()
# # ingredient2.name = 'Olive Oil'
# # ingredient3 = Ingredient()
# # ingredient3.name = 'Salt'

# # Append the ingredients with their quantities to the recipe using the proxy collection
# # new_recipe.ingredient_quantities.append((ingredient1, '2 breasts'))
# # new_recipe.ingredient_quantities.append((ingredient2, '2 tablespoons'))
# # new_recipe.ingredient_quantities.append((ingredient3, 'To taste'))
# # Create tuples with ingredient and quantity

# association1 = RecipeIngredient()
# association1.recipe_id = new_recipe.id
# association1.ingredient_id =  ingredient1.ingredient_id

# # Add likes and comments to the example recipe
# likes1 = Likes()
# likes1.user_id = user.id
# likes1.recipe_id = new_recipe.id
# new_recipe.likes.append(likes1)

# comments1 = Comments()
# comments1.user_id = user.id
# comments1.recipe_id = new_recipe.id
# comments1.comment_text = 'This recipe was amazing!'
# comments2 = Comments()
# comments2.user_id = user.id
# comments2.recipe_id = new_recipe.id
# comments2.comment_text = 'I tried this and it turned out great!'
# new_recipe.comments.append(comments1)
# new_recipe.comments.append(comments2)

# storage.new(new_recipe)
# storage.save()
