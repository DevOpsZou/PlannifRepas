import unittest
from app import create_app
from flask import request
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database
from unittest.mock import Mock, patch
from model.db import Db
from model.recipe import Recipe
from unittest import mock
from unittest.mock import MagicMock
from unittest import result

class test_routes(unittest.TestCase):
    
    def setUp(self):
       pass
    @mock.patch('model.recipe.Recipe', autospec=True)
    @mock.patch('model.db.Db', autospec=True)  
    def test_routes(self, mock_db, mock_recipe):
        dbMoke= mock_db('sqlite:///')
        self.recipe = mock_recipe(dbMoke)
        self.recipe.readPlat=MagicMock(return_value=["1", "recette","3"])
        self.recipe.readEntree=MagicMock(return_value=["1", "recette","3"])
        resultPlat=self.recipe.readPlat()
        resultEntree=self.recipe.readEntree()
        self.appMain = create_app(dbMoke, self.recipe)
        self.test = self.appMain.test_client(self)
              
        # self.routes =["/","/accueil"]
        # for route in self.routes :
        #     response= self.test.get(route)
        #     statuscode=response.status_code
        #     self.assertEqual(statuscode, 200)
        # with self.appMain.test_request_context('/displayRecipe/?id=5'):
        #      assert request.args['id'] == '5'
                     
        self.assertEqual(resultPlat, ["1", "recette","3"])
        self.assertEqual(resultEntree, ["1", "recette","3"])
   
 
