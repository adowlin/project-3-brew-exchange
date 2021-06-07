import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# Authentication functionality for Register, Login, Logout, Profile adapted
# from Code Institute Flask Mini Project coursework:
# https://github.com/adowlin/flask-task-manager/blob/master/app.py

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>/", methods=["GET", "POST"])
def profile(username):
    # Get the session user's username from DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    recipes = list(mongo.db.recipes.find({"user": username}))

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been logged out.")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_method": request.form.get("brew_method"),
            "roast_level": request.form.get("roast_level"),
            "grind_size": request.form.get("grind_size"),
            "coffee_weight": request.form.get("coffee_weight"),
            "water_weight": request.form.get("water_weight"),
            "time_mins": request.form.get("time_mins"),
            "time_secs": request.form.get("time_secs"),
            "description": request.form.get("description"),
            "user": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Has Been Added!")
        return redirect(url_for('profile', username=session['user']))

    brew_methods = mongo.db.brew_methods.find().sort("method_name", 1)
    roast_levels = [
        "Light", "Light-Medium", "Medium", "Medium-Dark", "Dark", "French"]
    grind_sizes = [
        "Fine", "Fine-Medium", "Medium", "Medium-Coarse", "Coarse"
    ]
    return render_template(
        "add_recipe.html", brew_methods=brew_methods,
        roast_levels=roast_levels, grind_sizes=grind_sizes
        )


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        update_recipe = {
            "recipe_method": request.form.get("brew_method"),
            "roast_level": request.form.get("roast_level"),
            "grind_size": request.form.get("grind_size"),
            "coffee_weight": request.form.get("coffee_weight"),
            "water_weight": request.form.get("water_weight"),
            "time_mins": request.form.get("time_mins"),
            "time_secs": request.form.get("time_secs"),
            "description": request.form.get("description"),
            "user": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, update_recipe)
        flash("Recipe Has Been Updated!")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    brew_methods = mongo.db.brew_methods.find().sort("method_name", 1)
    roast_levels = [
        "Light", "Light-Medium", "Medium", "Medium-Dark", "Dark", "French"]
    grind_sizes = [
        "Fine", "Fine-Medium", "Medium", "Medium-Coarse", "Coarse"
    ]

    return render_template(
        "edit_recipe.html", recipe=recipe, brew_methods=brew_methods,
        roast_levels=roast_levels, grind_sizes=grind_sizes
        )


@app.route("/delete/<recipe_id>", methods=["GET", "POST"])
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Has Been Deleted!")
    return redirect(request.referrer)


@app.route("/brew_methods")
def brew_methods():
    brew_methods = mongo.db.brew_methods.find()
    return render_template("brew_methods.html", brew_methods=brew_methods)


@app.route("/add_brew_method", methods=["GET", "POST"])
def add_brew_method():
    if request.method == "POST":
        brew_method = {
            "method_name": request.form.get("brew_method")
        }
        mongo.db.brew_methods.insert_one(brew_method)
        flash("Brew Method Has Been Added!")
        return redirect(url_for('brew_methods'))

    return render_template("add_brew_method.html")


@app.route("/delete_brew_method/<brew_method_id>", methods=["GET", "POST"])
def delete_brew_method(brew_method_id):
    mongo.db.brew_methods.remove({"_id": ObjectId(brew_method_id)})
    flash("Brew Method Has Been Deleted!")
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
