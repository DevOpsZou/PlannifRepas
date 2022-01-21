# from mysql.connector.errors import InternalError
from hashlib import md5
from model.db import Db
import hashlib


class User(Db):
    def __init__(self):
        super().__init__()
        
    #---------------------CRUD METHOD------------------------------------------------------------------------------#
        
    def read(self):
        self.cursor=self.getCursor()
        sqlp="SELECT * FROM utilisateur"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows
    
    def create(self, userData):
        """[cette methode sert à ajouter un utilisateur dans la base de données des users, table utilisateur]

        Args:
            userData ([dict]): [les infos de l'utilisateur]
        """
        
        self.cursor=self.getCursor()
        pwdc = hashlib.sha256(userData.get('pwd').encode('utf-8')).hexdigest()
        sql = """INSERT INTO utilisateur (nom, prenom, civilite, naissance, mail, numero, cplmt_numero, voie,
            cplmt_adresse, cp, ville, pays, password)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        val = (userData.get('nom'),  userData.get('prenom'), userData.get('civilite'), userData.get('date'), 
                userData.get('email'), userData.get('numero'), userData.get('cplmt_numero'), userData.get('voie'),
                userData.get('cplmt_adresse'), userData.get('cp'), userData.get('ville'), userData.get('pays'),
                pwdc)
            
        self.cursor.execute(sql, val)
        self.cursor.close()