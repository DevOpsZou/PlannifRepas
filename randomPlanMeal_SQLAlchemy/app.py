from flask import Flask, render_template
from model.recipe import Recipe
from model.db import Db
from controller.recipeController import RecipeController


def create_app(db, recipe):
    app = Flask(__name__)
  
    
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


    # app.run(host='0.0.0.0')
    return app

import os
from dotenv import load_dotenv



if __name__ == '__main__':
    
    db = Db(value=load_dotenv())
    recipe = Recipe(db)
    app= create_app(db, recipe)
    app.run("0.0.0.0")