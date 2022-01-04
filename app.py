from flask import Flask, render_template
from model.db import Db
from model.recipe import Recipe
from controller.recipeController import RecipeController




app = Flask(__name__)
recipe = Recipe()
recipeController = RecipeController()


@app.route("/")
def index():
    return render_template("index.html")


#---------------------------------CRUD DEPLACEMENT------------------------------#
@app.route("/accueil")
def displayPlanWeek():
    return recipeController.read(recipe)



@app.route('/displayRecipe/<int:id>', methods = ['GET', 'POST'])
def displayRecipe(id):
    return recipeController.readRecipe(recipe, id)



