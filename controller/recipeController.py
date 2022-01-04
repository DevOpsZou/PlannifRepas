from flask import render_template




class RecipeController():
    def __init__(self):
        self.iddeplacement=None
        

    def read(self, recipe):
       
        result = recipe.read()
        
        return render_template("accueil.html", data= result, len=len(result))
        
    def readRecipe(self, recipe, id):
       
        result = recipe.readRecipe(id)
        print(result)
        return render_template("displayRecipe.html", data= result, len=len(result))
        
