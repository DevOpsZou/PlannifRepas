
from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash, render_template
'''
Authors : Zoubida AFOUTNI
Date : 13/01/2022

'''
class Controlleur():
    def login(self, model, email, password):
        user = model.getUserByEmail(email)
        if user:
            if check_password_hash(user.password, password):
                return render_template("accueil.html")
            else :
                flash('Mot de passe incorrect.', category='error')
        else:
           
            flash('Cet email n\'existep pas.', category='error')
        
        return render_template("index.html")