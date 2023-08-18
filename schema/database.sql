-- creates database for the project

CREATE DATABASE IF NOT EXISTS virtual_recipe_meal;
CREATE USER IF NOT EXISTS 'recipe'@'localhost' IDENTIFIED BY 'recipe_pwd';
GRANT ALL ON virtual_recipe_meal.* TO 'recipe'@'localhost';
GRANT SELECT ON performance_schema.* TO 'recipe'@'localhost';
