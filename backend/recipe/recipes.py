from flask import Flask, render_template, request, url_for, redirect 
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient(f"mongodb+srv://sbloodworth:cvcnLUFIZ99cnlpb@dinein.hedhcr9.mongodb.net/")

#Index Route
@app.route("/recipes/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        title = request.form['title']
        ingredients = request.form['ingredients']
        steps = request.form['steps']
        category = request.form['category']

        recipes.insert_one({'title': title, 'ingredients': ingredients, 'steps': steps, 'category': category})
        return redirect(url_for('index'))
    all_items = recipes.find()
    return render_template('index.html', items = all_items)

#Delete Route
@app.post("/recipes/<id>/delete/")
def delete(id):
    recipes.delete_one({"_id":ObjectId(id)})
    return redirect(url_for('index'))

#Update Route
@app.post("/recipes/<id>/update/")
def update(id):

    _id = ObjectId(id)

    if request.method == "POST":
        update_title = request.form['update_title']
        update_ingredients = request.form['update_ingredients']
        update_steps = request.form['update_steps']
        update_category = request.form['update_category']

    all_updates = {
        "$set": {"title": update_title,
                "ingredients": update_ingredients,
                "steps": update_steps,
                "category": update_category,
                }
    }

    recipes.update_one({"id": id}, all_updates)

    return redirect(url_for('index'))

db = client.RECIPES
recipes = db.recipes

#recipes.insertone({'title': "pbj", 'ingredients': ["peanut butter", "jelly", "bread"], 'steps': ["spread spreads on bread", "smoosh together", "eat"], 'category': "Quick Eats"})

if __name__ == "__main__":
    app.run(debug=True)
