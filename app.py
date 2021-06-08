import os
from functools import wraps
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


# Login Required decorator from Flask:
# https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator
# https://github.com/TravelTimN/flask-task-manager-project/blob/demo/app.py
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # User not logged in
        if "user" not in session:
            flash("Please log in to view this page!")
            return redirect(url_for("login"))
        # User is logged in
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template(
        "recipes.html", recipes=recipes, page_header="Search Recipes")


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template(
        "recipes.html", recipes=recipes, scroll="search-header")


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
    return render_template("register.html", page_header="Register")


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

    return render_template("login.html", page_header="Log In")


@app.route("/profile/<username>/", methods=["GET", "POST"])
@login_required
def profile(username):
    if session["user"] == username:
        # Get the session user's username from DB
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # Get the recipes created by this user
        recipes = list(mongo.db.recipes.find({"user": username}))
        return render_template(
            "profile.html", username=username,
            recipes=recipes, page_header="Your Recipes")
    else:
        # If user is not the same as username in URL, redirect to own profile
        flash("You do not have permission to view that page.")
        return redirect(url_for("profile", username=session["user"]))


@app.route("/logout")
@login_required
def logout():
    # Remove user from session cookies
    flash("You have been logged out.")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
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
        roast_levels=roast_levels, grind_sizes=grind_sizes,
        page_header="Add New Recipe")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # Check if user matches the user who owns the recipe
    if session["user"] == recipe["user"]:
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
            mongo.db.recipes.update(
                {"_id": ObjectId(recipe_id)}, update_recipe)
            flash("Recipe Has Been Updated!")

        brew_methods = mongo.db.brew_methods.find().sort("method_name", 1)
        roast_levels = [
            "Light", "Light-Medium", "Medium", "Medium-Dark", "Dark", "French"]
        grind_sizes = [
            "Fine", "Fine-Medium", "Medium", "Medium-Coarse", "Coarse"
        ]

        return render_template(
            "edit_recipe.html", recipe=recipe, brew_methods=brew_methods,
            roast_levels=roast_levels, grind_sizes=grind_sizes,
            page_header="Edit Recipe")
    else:
        flash("You don't have permission to edit this recipe")
        return redirect(url_for("profile", username=session["user"]))


@app.route("/delete/<recipe_id>", methods=["GET", "POST"])
@login_required
def delete_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # Check if user matches the user who owns the recipe
    if session["user"] == recipe["user"]:
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        flash("Recipe Has Been Deleted!")
        return redirect(request.referrer)
    else:
        flash("You don't have permission to delete this recipe.")
        return redirect(url_for("profile", username=session["user"]))


@app.route("/brew_methods")
@login_required
def brew_methods():
    # Check if user is "admin"
    if session["user"] == "admin":
        brew_methods = mongo.db.brew_methods.find()
        return render_template(
            "brew_methods.html", brew_methods=brew_methods,
            page_header="Manage Brew Methods")
    else:
        flash("You do not have permission to view that page.")
        return redirect(url_for("profile", username=session["user"]))


@app.route("/add_brew_method", methods=["GET", "POST"])
@login_required
def add_brew_method():
    # Check if user is "admin"
    if session["user"] == "admin":
        if request.method == "POST":
            brew_method = {
                "method_name": request.form.get("brew_method")
            }
            mongo.db.brew_methods.insert_one(brew_method)
            flash("Brew Method Has Been Added!")
            return redirect(url_for('brew_methods'))

        return render_template(
            "add_brew_method.html", page_header="Add A Brew Method")
    else:
        flash("You do not have permission to view that page.")
        return redirect(url_for("profile", username=session["user"]))


@app.route("/delete_brew_method/<brew_method_id>", methods=["GET", "POST"])
@login_required
def delete_brew_method(brew_method_id):
    # Check if user is "admin"
    if session["user"] == "admin":
        mongo.db.brew_methods.remove({"_id": ObjectId(brew_method_id)})
        flash("Brew Method Has Been Deleted!")
        return redirect(url_for('brew_methods'))
    else:
        flash("You do not have permission to view that page.")
        return redirect(url_for("profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
