
from sqlalchemy.orm import sessionmaker, Session, load_only
import pymysql
from sqlalchemy.ext.automap import automap_base
from model.db import Db
from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.orm import defer
from sqlalchemy.orm import undefer
from sqlalchemy.sql.expression import func

class Recipe(Db):
    def __init__(self):
       super().__init__()
      
    
    def readPlat(self):
     
        self.resultQuety=[]
        self.test=self.session.query(self.Recette).\
            with_entities(self.Recette.id_recette, self.Recette.nom_recette, self.Categorie.nom_categorie).\
            join(self.Categorie).\
            filter(self.Categorie.nom_categorie.like("Plat principal")).\
                order_by(func.rand()).limit(14)
        self.result=self.test.all()
        for ele in self.result:
            element=dict(ele)
            self.resultQuety.append(element)
           
        return  self.resultQuety
    
    def readEntree(self):
         
        self.resultQuety=[]
        self.test=self.session.query(self.Recette).\
            with_entities(self.Recette.id_recette, self.Recette.nom_recette, self.Categorie.nom_categorie).\
            join(self.Categorie).\
            filter(self.Categorie.nom_categorie.like("Entree")).\
                order_by(func.rand()).limit(14)
        self.result=self.test.all()
        for ele in self.result:
            element=dict(ele)
            self.resultQuety.append(element)
           
        return  self.resultQuety
    
    def readRecipe(self, id):
        self.resultQuety=[]
        
        dictRecipe ={}
        dictIngredients={}
        rowsIngredients=[]
     
        self.test=self.session.query(self.Recette).\
            with_entities(self.Recette.id_recette, self.Recette.nom_recette, self.Recette.duree_recette,
                          self.Ingredient.nom_ingredient, self.Recette_ingredient.quantite, 
                          self.Recette_ingredient.mesure, self.Etapes.etape_desc).\
            join(self.Recette_ingredient, self.Recette_ingredient.fk_id_recette==self.Recette.id_recette).\
                join(self.Ingredient, self.Ingredient.id_ingredient==self.Recette_ingredient.fk_id_ingredient).\
                join(self.Etapes, self.Etapes.fk_id_recette=={id}).\
            filter(self.Recette.id_recette=={id})
        
        self.result=self.test.all()
        for ele in self.result:
            element=dict(ele)
            self.resultQuety.append(element)

        for elem in  self.resultQuety:
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
      
       
       
        return  dictRecipe

