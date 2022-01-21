import mysql.connector
from model.config import Config

class Db():
    
    def __init__(self):
        self.logging()

    def logging(self):
        self.conn = mysql.connector.connect(
            user=Config.user,
            password=Config.password,
            host=Config.host,
            database=Config.database,
            port=Config.port
            )
        self.conn.autocommit=True
        

    def getCursor(self):
        try:
            cursor = self.conn.cursor(dictionary=True)
            return cursor
        except mysql.connector.Error as err:
            print(err)
        self.conn.autocommit=True

# from sqlalchemy import create_engine, Table 
# from sqlalchemy.orm import sessionmaker, Session  
# import pymysql 
# from sqlalchemy.ext.automap import automap_base    

# class Dbal():     
#     def init(self): 
#         self.logging()
        
#     def logging(self):      
#         self.engine = create_engine('mysql+pymysql://root:formation@localhost:3306/projet')         
#         self.Base = automap_base()         
#         self.Base.prepare(self.engine, reflect=True)         
#         self.DBSession = sessionmaker(bind=self.engine)         
#         self.session = self.DBSession()         
#         self.tablename = Table('utilisateur', self.Base.metadata,autoload=True, autoload_with=self.engine) 
        
#     def readuser(self):                 
#         return self.session.query(self.tablename).all()
    
