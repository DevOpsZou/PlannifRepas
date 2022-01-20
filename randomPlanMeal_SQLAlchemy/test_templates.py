import unittest

from app import app
from flask import request
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database
from model.db import Db
from model.recipe import Recipe
from unittest.mock import Mock, patch


class test_routes(unittest.TestCase):
    # def setUp(self):
    #     self.db = Db()
    #     self.recipe = Recipe()
    
    def test_routes(self):
        test=app.test_client(self)
        routes =["/","/accueil","/entree", "/plat", "/plat"]
        for route in routes :
            response= test.get(route)
            statuscode=response.status_code
            self.assertEqual(statuscode, 200)
        with app.test_request_context('/displayRecipe/?id=5'):
             assert request.args['id'] == '5'
   
    def test_content(self):
        test=app.test_client(self)
        routes =["/","/accueil","/entree", "/plat", "/plat"]
        for route in routes :
            response= test.get(route)
            content=response.content_type
            self.assertEqual(content, "text/html; charset=utf-8")      
    
    # @pytest.fixture(scope="function")
    # def SessionLocal():
    #     TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///./test_temp.db"
    #     assert database_exists(TEST_SQLALCHEMY_DATABASE_URL), "Test database already exists. Aborting tests."
   
   
    # @patch('model.db.Db.logging')
    # def test_get_data(self, mock_db):
    #     mock_db.return_value.query_all_data.return_value = "[{'id_recette': 6862, 'nom_recette': 'Sau[1401 chars]al'}] !"
    #     result = self.recipe.readPlat()

    #     self.assertEqual( mock_db.return_value.query_all_data.return_value,  "[{'id_recette': 6862, 'nom_recette': 'Sau[1401 chars]al'}] !")
      
    #     self.assertEqual(mock_db.call_count,'1')
    #     self.assertEqual(mock_db.query_all_data.call_count, 1)    
    
    # def test_get_data(self):
      
    #     with patch('model.db.Db.logging', return_value=Mock()) as mock_db:
           
    #         mock_db.return_value.readPlat.return_value = 'result ooo'
    #         print( mock_db.return_value.readPlat.return_value )
    #         # result = get_data()
    #         # self.assertEqual("result", 'result data')
    #         self.assertEqual(mock_db.call_count, '1')
    #         self.assertEqual(mock_db.query_all_data.call_count, 1)
# if __name__ == '__main__':
   
#     unittest.main()