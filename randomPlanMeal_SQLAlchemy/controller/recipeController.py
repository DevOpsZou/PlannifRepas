from flask import render_template, jsonify

class RecipeController():
    def __init__(self):
        self.iddeplacement=None
    def readPlat(self, recipe):
        result = recipe.readPlat()
        print(type(result))
        print (type(jsonify(result)))
        # return render_template("plat.html", data= result, len=len(result))
        return jsonify(result)
    
    def readEntree(self, recipe):
        result = recipe.readEntree()
        # return render_template("entree.html", data= result, len=len(result))
        return jsonify(result)
    def readRecipe(self, recipe, id):
        result = recipe.readRecipe(id)
        return jsonify(result)
        # return render_template("displayRecipe.html", data= result, len=len(result))
 


            