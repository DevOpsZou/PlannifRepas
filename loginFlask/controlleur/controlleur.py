
import os
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
                #flash('Logged in successfully!', category='success')
                return render_template("accueil.html")
            else:
                return flash('Incorrect password, try again.', category='error')
        else:
            return flash('Email does not exist.', category='error')
        