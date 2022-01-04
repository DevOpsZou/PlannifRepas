from model.db import Db

class Recipe(Db):
    def __init__(self):
        super().__init__()
    
    
    #-------------------CRUD METHOD------------------------------------------------#
    def read(self):
        self.cursor=self.getCursor()
        sqlp=f"""SELECT id_recette, nom_recette FROM recette ORDER BY RAND() LIMIT 14;"""
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows
    
    def readRecipe(self, id):
        self.cursor=self.getCursor()
        sqlp=f"""SELECT id_recette, nom_recette, duree_recette, nom_ingredient, etape_desc FROM recette 
        join ingredient on ingredient.fk_id_recette=id_recette  
        join etapes on etapes.fk_id_recette=id_recette 
        where id_recette={id};"""
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows