
import os
import pymysql
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, Session, load_only, undefer, defer
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.sql.expression import func

'''
Authors : Zoubida AFOUTNI
Date : 13/01/2022
'''
class Db():
    
    def __init__(self, value):
        
        self.url=value
        self.logging()
      
    @property
    def url(self):
        return self._url
 
    @url.setter
    def url(self, value):
        self._url = "%s://%s:%s@%s:%s/%s" % (
        os.getenv("DRIVER"),
        os.getenv("MYSQL_DATABASE_USER"),
        os.getenv("MYSQL_ROOT_PASSWORD"),
        os.getenv("MYSQL_SERVICE_HOST"),
        int(os.getenv("MYSQL_DATABASE_PORT")),
        os.getenv('DB_NAME')
    )
    

    def logging(self):
        """[contains code to connect to database : recettebis]
        """
        if self.url != "sqlite:///" :
            print(self.url)
            self.engine = create_engine(self.url)
            self.DBSession = sessionmaker(bind=self.engine)
            self.session = self.DBSession()
            self.metadata = MetaData()
            self.metadata.reflect(self.engine)
            self.Base = automap_base(metadata=self.metadata)
            self.metadata.reflect(self.engine)
            self.Base.prepare()
            self.Recette = self.Base.classes.recette
            self.Categorie = self.Base.classes.categorie
            self.Recette_ingredient=self.Base.classes.recette_ingredients
            self.Ingredient=self.Base.classes.ingredient
            self.Etapes=self.Base.classes.etapes