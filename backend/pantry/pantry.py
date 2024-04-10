from flask import Flask, render_template, request, url_for, redirect 
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient(f"mongodb+srv://sbloodworth:cvcnLUFIZ99cnlpb@dinein.hedhcr9.mongodb.net/")

#Index Route
@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        unit = request.form['unit']
        tags = request.form['tags']
        image_url = request.form['image_url']
        expiration_date = request.form['expiration_date']

        items.insert_one({'item_name': item_name, 'quantity': quantity, 'unit': unit, 'tags': tags, 'image_url': image_url, 'expiration_date': expiration_date})
        return redirect(url_for('index'))
    all_items = items.find()
    return render_template('index.html', items = all_items)

#Delete Route
@app.post("/<id>/delete/")
def delete(id):
    items.delete_one({"_id":ObjectId(id)})
    return redirect(url_for('index'))

#Update Route
@app.post("/<id>/update/")
def update(id):

    _id = ObjectId(id)

    if request.method == "POST":
        update_item_name = request.form['update_item_name']
        update_quantity = request.form['update_quantity']
        update_unit = request.form['update_unit']
        update_tags = request.form['update_tags']
        update_image_url = request.form['update_image_url']
        update_expiration_date = request.form['update_expiration_date']

    all_updates = {
        "$set": {"item_name": update_item_name,
                "quantity": update_quantity,
                "unit": update_unit,
                "tags": update_tags,
                "image_url": update_image_url,
                "expiration_date": update_expiration_date}
    }

    items.update_one({"_id": _id}, all_updates)

    return redirect(url_for('index'))

db = client.PANTRY
items = db.items

if __name__ == "__main__":
    app.run(debug=True) #running your server on development mode, setting debug to True