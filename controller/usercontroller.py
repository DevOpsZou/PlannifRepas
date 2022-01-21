from flask import render_template
from werkzeug.utils import redirect
# from model.user import User

class userController():
    def __init__(self):
        self.iduser=None
        
    def create(self):
        return render_template("inscription.html")
    
    def treateCreate(self, user, data):
        user.create(data)
        return redirect("/")
    
    def connexion(self):
        pass
    
