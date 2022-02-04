from flask import render_template, jsonify

class RecipeController():
    def __init__(self):
        pass
    def readPlat(self, recipe):
        result = recipe.readPlat()
        return jsonify(result)
    
    def readEntree(self, recipe):
        result = recipe.readEntree()
        # return render_template("entree.html", data= result, len=len(result))
        return jsonify(result)
    def readRecipe(self, recipe, id):
        result = recipe.readRecipe(id)
        return jsonify(result)
        # return render_template("displayRecipe.html", data= result, len=len(result))
 


            