from model.db import Db

class Recipe(Db):
    def __init__(self):
        super().__init__()
    
    
    #-------------------CRUD METHOD------------------------------------------------#
    def readPlat(self):
        self.cursor=self.getCursor()
        rows=[]
        queryPlat=f"""SELECT id_recette, nom_recette, nom_categorie FROM recette join categorie 
        on recette.fk_id_categorie = categorie.id_categorie 
        and nom_categorie ='Plat principal' ORDER BY RAND() LIMIT 14"""
        self.cursor.execute(queryPlat)
        for elem in self.cursor.fetchall():
            rows.append(elem)
        self.cursor.close()
      
        return rows

    def readEntree(self):
        self.cursor=self.getCursor()
        rows=[]
        queryEntree=f"""SELECT id_recette, nom_recette, nom_categorie FROM recette join categorie 
        on recette.fk_id_categorie = categorie.id_categorie 
        and nom_categorie ='Entree' ORDER BY RAND() LIMIT 14"""
        # queries = [queryPlat, queryEntree]
        # for query in queries :
        self.cursor.execute(queryEntree)
        for elem in self.cursor.fetchall():
            rows.append(elem)
        self.cursor.close()
      
        return rows
        
    
    def readRecipe(self, id):
        self.cursor = self.getCursor()
        rows = []
        rowsIngredients = []
        dictRecipe={}
        sqlp = f"""SELECT id_recette, nom_recette, duree_recette, nom_ingredient, quantite, mesure
        FROM recette 
        join recette_ingredient on recette_ingredient.fk_id_recette=id_recette 
        join ingredient on recette_ingredient.fk_id_ingredient = ingredient.id_ingredient
      
        where id_recette={id};"""
        sqlEtape = f""" SELECT etape_desc FROM etapes where etapes.fk_id_recette = {id};"""
        dictRecipe ={}
        dictIngredients={}
        queries = [sqlp, sqlEtape]
        for query in queries :
            self.cursor.execute(query)
            for elem in self.cursor.fetchall():
                for k, v in elem.items() :
                   if k == "nom_ingredient" :
                        dictIngredients={}
                        dictIngredients["nom_ingredient"]=elem.get("nom_ingredient")
                       
                   elif k == "id_recette" :
                        dictRecipe["id_recette"] = elem.get("id_recette")
                   elif k == "nom_recette" :
                        dictRecipe["nom_recette"] = elem.get("nom_recette")
                   elif k == "quantite" :
                        dictIngredients["quantite"] = elem.get("quantite")
                   elif k == "mesure" :
                        dictIngredients["mesure"] = elem.get("mesure")
                       
                        rowsIngredients.append(dictIngredients)
                   elif k == "etape_desc" :
                       dictRecipe["etape_desc"] = elem.get("etape_desc")
                   elif k == "duree_recette" :
                        dictRecipe["duree_recette"] = elem.get("duree_recette")
                  
        dictRecipe["nom_ingredient"] = rowsIngredients        
        self.cursor.close()
       
       
        return dictRecipe