from flask import render_template




class RecipeController():
    def __init__(self):
        self.iddeplacement=None
        

    def readEntree(self, recipe):
        
        result = recipe.readEntree()
        
        return render_template("entree.html", data= result, len=len(result))
    
    def readPlat(self, recipe):
            
        result = recipe.readPlat()
        
        return render_template("plat.html", data= result, len=len(result))
    
        
    def readRecipe(self, recipe, id):
       
        result = recipe.readRecipe(id)
       
        return render_template("displayRecipe.html", data= result, len=len(result))
 


            