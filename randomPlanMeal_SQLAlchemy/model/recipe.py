
import pymysql
from sqlalchemy.orm import sessionmaker, Session, load_only
from sqlalchemy.ext.automap import automap_base
from model.db import Db
from sqlalchemy import create_engine, MetaData, Table, Column, distinct
from sqlalchemy.orm import defer, undefer
from sqlalchemy.sql.expression import func


class Recipe():
    def __init__(self,db):
        self.db=db
      
  
    def readPlat(self):
        self.resultQuety=[]
        self.test=self.db.session.query(self.db.Recette).\
            with_entities(self.db.Recette.id_recette, self.db.Recette.nom_recette, self.db.Categorie.nom_categorie).\
            join(self.db.Categorie).\
            filter(self.db.Categorie.nom_categorie.like("Plat principal")).distinct().\
                order_by(func.rand()).limit(14)
        self.result=self.test.all()
        for ele in self.result:
            element=dict(ele)
            self.resultQuety.append(element)
           
        return  self.resultQuety
    
    def readEntree(self):
        self.resultQuety=[]
        self.test=self.db.session.query(self.db.Recette).\
            with_entities(self.db.Recette.id_recette, self.db.Recette.nom_recette, self.db.Categorie.nom_categorie).\
            join(self.db.Categorie).\
            filter(self.db.Categorie.nom_categorie.like("Entree")).distinct().\
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
     
        self.test=self.db.session.query(self.db.Recette).\
            with_entities(self.db.Recette.id_recette, self.db.Recette.nom_recette, self.db.Recette.duree_recette,
                          self.db.Ingredient.nom_ingredient, self.db.Recette_ingredient.quantite, 
                          self.db.Recette_ingredient.mesure, self.db.Etapes.etape_desc).\
            join(self.db.Recette_ingredient, self.db.Recette_ingredient.fk_id_recette==self.db.Recette.id_recette).\
                join(self.db.Ingredient, self.db.Ingredient.id_ingredient==self.db.Recette_ingredient.fk_id_ingredient).\
                join(self.db.Etapes, self.db.Etapes.fk_id_recette=={id}).\
            filter(self.db.Recette.id_recette=={id})
        
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

