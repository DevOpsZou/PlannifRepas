from flask import render_template




class RecipeController():
    def __init__(self):
        self.iddeplacement=None
        

    def read(self, recipe):
        print("JE suis la")
        result = recipe.read()
        
        return render_template("displayPlanWeek.html", data= result, len=len(result))
        
    def readRecipe(self, recipe, id):
        print("JE suis la")
        result = recipe.readRecipe(id)
        print(result)
        return render_template("displayRecipe.html", data= result, len=len(result))
        
