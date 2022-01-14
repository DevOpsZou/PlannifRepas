from flask import Flask, render_template

from model.recipe import Recipe
from controller.recipeController import RecipeController




app = Flask(__name__)

recipe = Recipe() 
recipeController = RecipeController()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/accueil")
def displayPlanWeek():
    return render_template("accueil.html")


@app.route("/entree")
def displayPlanWeekentree():
    return recipeController.readEntree(recipe)


@app.route("/plat")
def displayPlanWeekplat():
    return recipeController.readPlat(recipe)

@app.route('/displayRecipe/<int:id>', methods = ['GET', 'POST'])
def displayRecipe(id):
    return recipeController.readRecipe(recipe, id)



<<<<<<<< HEAD:randomPlanMeal_SQLAlchemy/app.py
app.run()
========
app.run(host='0.0.0.0')
>>>>>>>> 0ccab6580c97f5456da25847d0b0bdfab29e9adf:randomPlanMeal_MySqlConnector/app.py
