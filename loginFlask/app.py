from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for, jsonify
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager

from sqlalchemy import insert

from flask_sqlalchemy import SQLAlchemy
from os import path

from model.db import Db
# from consul import Consul
import os
from dotenv import load_dotenv

DEBUG_MODE=os.environ.get("DEBUG_MODE", "True")
SERVER_PORT=os.environ.get("SERVER_PORT", "80")
SERVER_HOST=os.environ.get("SERVER_HOST", "0.0.0.0")
CONSUL_HOST=os.environ.get("CONSUL_HOST", "localhost")
CONSUL_PORT=os.environ.get("CONSUL_PORT", "9500")

def create_app():
    app = Flask(__name__)
    db = Db()
    app.secret_key = 'asrtarstaursdlarsn'
    app.config['SECRET_KEY'] = 'asrtarstaursdlarsn'
 
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # @app.get("/admin")
    # def log():
    #     response = requests.get(f"http://randommeal:80/planifrepas/plat")
    #     return jsonify(response.json())
    @app.route ("/admin", methods=['GET', 'POST'])
    def login():
        listItem=[]
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('pwd')
      
            user=db.session.query(db.User).filter(db.User.email==email).first()

            if user:
                if check_password_hash(user.password, password):
                    flash('Logged in successfully!', category='success')
                    return render_template("accueil.html")
                                   
                else:
                    flash('Incorrect password, try again.', category='error')
            else:
            
                flash('Email does not exist.', category='error')
    
        return render_template("index.html", user=current_user)

    @app.route('/admin/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('auth.login'))
    
    
    #Routes random meal#########################################################################""   
    @app.route('/admin/plat')
    def displayPlat():
        listItem=[]
        response = requests.get(f"http://randommeal:80/planifrepas/plat")
        for i in response.json():
            listItem.append(i)
        return render_template("plat.html",data =listItem, len = len(listItem))
    
    @app.route('/admin/entree')
    def displayEntree():
        listItem=[]
        response = requests.get(f"http://randommeal:80/planifrepas/entree")
        for i in response.json():
            listItem.append(i)
        return render_template("plat.html",data =listItem, len = len(listItem))
    
    @app.route('/admin/displayRecipe/<int:id>')
    def displayRecipe(id):
        listItem=[]
        response = requests.get(f"http://randommeal:80/planifrepas/displayRecipe/{id}")
        for i in response.json():
            listItem.append(i)
        return render_template("displayRecipe.html",data =response.json())
    #Routes random meal####################################################################################
    
    @app.route('/admin/sign-up',  methods=['GET', 'POST'])
    def sign_up():
        if request.method == 'POST':
            email = request.form.get('email')
            first_name = request.form.get('nom')
            password1 = request.form.get('pwd')
            password2 = request.form.get('pwd')

            user = db.session.query(db.User).filter(db.User.email==email).first()
            if user:
                flash('Email already exists.', category='error')
            elif len(email) < 4:
                flash('Email must be greater than 3 characters.', category='error')
            elif len(first_name) < 2:
                flash('First name must be greater than 1 character.', category='error')
            elif password1 != password2:
                flash('Passwords don\'t match.', category='error')
            elif len(password1) < 7:
                flash('Password must be at least 7 characters.', category='error')
            else:
                stmt = (
                    insert(db.User).
                    
                    values(email=email, first_name=first_name, password=generate_password_hash(
                     password1, method='sha256') )
                    )
                db.engine.execute(stmt)
                flash('Account created!', category='success')
                return redirect(url_for('login'))

        return render_template("inscription.html", user=current_user)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

if __name__ == '__main__':
    app= create_app()
    app.run(host=SERVER_HOST, port=int(SERVER_PORT), debug=bool(DEBUG_MODE))

