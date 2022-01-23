from flask import Flask, render_template, request, Response
from model.recipe import Recipe
from model.db import Db
from controller.recipeController import RecipeController
# from consul import Consul
import os
from dotenv import load_dotenv

DEBUG_MODE=os.environ.get("DEBUG_MODE", "False")
SERVER_PORT=os.environ.get("SERVER_PORT", "80")
SERVER_HOST=os.environ.get("SERVER_HOST", "0.0.0.0")
CONSUL_HOST=os.environ.get("CONSUL_HOST", "localhost")
CONSUL_PORT=os.environ.get("CONSUL_PORT", "9500")
def create_app(db, recipe):
    app = Flask("randommeal")
  
    
    recipeController = RecipeController()

    @app.get("/planifrepas")
    def index():
        return render_template("index.html")

    @app.get("/planifrepas/accueil")
    def displayPlanWeek():
        return render_template("accueil.html")

    @app.get("/planifrepas/entree")
    def displayPlanWeekentree():
        return recipeController.readEntree(recipe)

    @app.get("/planifrepas/plat")
    def displayPlanWeekplat():
        return recipeController.readPlat(recipe)

    @app.route('/planifrepas/displayRecipe/<int:id>')
    def displayRecipe(id):
        return recipeController.readRecipe(recipe, id)

    return app

if __name__ == '__main__':
    db = Db(value=load_dotenv())
    recipe = Recipe(db)
    app= create_app(db, recipe)
    app.run(host=SERVER_HOST, port=int(SERVER_PORT), debug=bool(DEBUG_MODE))