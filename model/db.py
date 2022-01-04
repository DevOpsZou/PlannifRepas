import mysql.connector
import os
from dotenv import load_dotenv

class Db():
    
    def __init__(self):
        self.logging()

    def logging(self):
        
        load_dotenv()
      
        self.conn = mysql.connector.connect(
                user=os.getenv('USER'),
                password=os.getenv('PASSWORD'),
                host = os.getenv('HOST'),
                database=os.getenv('DATABASE')
            )
        
        self.conn.autocommit=True
            
         #il est à zero par defaut sur mysql.connector  

    def getCursor(self):
        try:
            cursor = self.conn.cursor(dictionary=True)
            return cursor
        except mysql.connector.Error as err:
            print(err)
        self.conn.autocommit=True
           
        
     


