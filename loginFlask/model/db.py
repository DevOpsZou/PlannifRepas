
import os
from dotenv import load_dotenv
from flask_login import UserMixin
import pymysql
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import sessionmaker, Session, load_only
'''
Authors : Zoubida AFOUTNI
Date : 13/01/2022
'''
class Db():
    
    def __init__(self, value=load_dotenv()):
      
        self.url=value
        self.logging()
      
    @property
    def url(self):
        return self._url
 
    @url.setter
    def url(self, value):
        self._url = "%s://%s:%s@%s:%s/%s" % (
        "mysql+pymysql",
        os.getenv("MYSQL_DATABASE_USER"),
        os.getenv("MYSQL_ROOT_PASSWORD"),
        os.getenv("MYSQL_SERVICE_HOST"),
        int(os.getenv("MYSQL_DATABASE_PORT")),
        os.getenv('DB_NAME')
    )
   

    def logging(self):
        """[contains code to connect to database : recettebis]
        """
        print(self.url)
        self.engine = create_engine(self.url)
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()
        self.metadata = MetaData()
        self.metadata.reflect(self.engine)
        self.Base = automap_base(metadata=self.metadata)
        self.metadata.reflect(self.engine)
        self.Base.prepare()

        self.User = self.Base.classes.user
     
    
 
     


