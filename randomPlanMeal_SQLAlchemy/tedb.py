# conftest.py

import pytest
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import create_app

class test_routes():
    def setUp(self):
        self.appMain = create_app()
    
    # def test_routes(self):
        
    #     test = self.appMain.test_client(self)
    #     routes =["/","/accueil"]
    #     # routes =["/","/accueil"]
    #     for route in routes :
    #         response= test.get(route)
    #         statuscode=response.status_code
        
    #         self.assertEqual(statuscode, 200)
    @pytest.fixture(scope="session")
    def engine():
        print("TestCase: Using sqlite database")
        return create_engine('sqlite:///', echo=False)


    @pytest.fixture(scope="session")
    def session(engine):
        sessionmaker_ = sessionmaker(bind=engine)
        session = sessionmaker_()
        Base.metadata.create_all(engine)

        metadata = MetaData()
        metadata.reflect(engine)
        Base = automap_base(metadata=metadata)
        metadata.reflect(engine)
        Base.prepare()

        Recette = Base.classes.recette
        Categorie = Base.classes.categorie
        Recette_ingredient=Base.classes.recette_ingredients
        Ingredient=Base.classes.ingredient
        Etapes=Base.classes.etapes
    
    
        test = session.query(Recette).\
                with_entities(Recette.id_recette, Recette.nom_recette, Categorie.nom_categorie).\
                join(Categorie).\
                filter(Categorie.nom_categorie.like("Plat principal")).\
                    order_by(func.rand()).limit(14)
        result=test.all()
        self.assertEqual( result,  "[{'id_recette': 6862, 'nom_recette': 'Sau[1401 chars]al'}] !")
        # yield session

        # session.close()
 # @mock.patch('model.db.Db', autospec=True)
    # def test_get_data(self, mock_db):
    #     print(mock_db)
    #     # mock_db.return_value.readPlat.return_value = "[{'id_recette': 6862, 'nom_recette': 'Sau[1401 chars]al'}] !"
    #     recipe = Recipe(db=mock_db)
    #     # print(recipe.readPlat())

        # self.assertEqual( "[{'id_recette': 6862, 'nom_recette': 'Sau[1401 chars]al'}] !",  "[{'id_recette': 6862, 'nom_recette': 'Sau[1401 chars]al'}] !")

# if __name__=="__main__":

#     unittest.main()

test =  test_routes()