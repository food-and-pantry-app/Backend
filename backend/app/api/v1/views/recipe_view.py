# /app/views/recipe_view.py
# from flask import Blueprint, jsonify, request
# from app.controllers.recipe_controller import get_all_recipes, get_recipe
#
# recipe_blueprint = Blueprint('recipes', __name__)
#
# @recipe_blueprint.route('/recipes', methods=['GET'])
# def show_recipes():
#     """Endpoint to get all recipes"""
#     recipes = get_all_recipes()
#     return jsonify([recipe.__dict__ for recipe in recipes])
#
# @recipe_blueprint.route('/recipes/<int:recipe_id>', methods=['GET'])
# def show_recipe(recipe_id):
#     """Endpoint to get a specific recipe by ID"""
#     recipe = get_recipe(recipe_id)
#     if recipe:
#         return jsonify(recipe.__dict__)
#     return jsonify({"error": "Recipe not found"}), 404
