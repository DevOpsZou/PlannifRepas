from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for, jsonify
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from sqlalchemy import insert
from flask_sqlalchemy import SQLAlchemy
from model.db import Db
from model.model import Model
from controlleur.controlleur import Controlleur
import os
from dotenv import load_dotenv
import random

DEBUG_MODE=os.environ.get("DEBUG_MODE", "True")
SERVER_PORT=os.environ.get("SERVER_PORT", "80")
SERVER_HOST=os.environ.get("SERVER_HOST", "0.0.0.0")
CONSUL_HOST=os.environ.get("CONSUL_HOST", "localhost")
CONSUL_PORT=os.environ.get("CONSUL_PORT", "9500")
RANDOM_HOST=os.environ.get("RANDOM_HOST", "randommeal")
PORT_HOST=int(os.environ.get("PORT_HOST", "80"))

def create_app():
    controlleur=Controlleur()
    app = Flask(__name__)
    db = Db()
    model = Model(db)
    app.secret_key = 'asrtarstaursdlarsn'
    app.config['SECRET_KEY'] = 'asrtarstaursdlarsn'
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @app.route ("/home")
    def home():
        return render_template("index.html")
    @app.route ("/", methods=['GET', 'POST'])
    def login():
        print("La methode ", request.method)
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('pwd')
            return controlleur.login(model, email, password)
        else :
            return render_template("index.html", user=current_user)
    
       
       
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('auth.login'))
    
    @app.route('/construction')
    def construction():
        return render_template("construction.html")
    
    #Routes random meal#########################################################################""   
    @app.route('/plat')
    def displayPlat():
        listItem=[]
        response = requests.get(f"http://{RANDOM_HOST}:{PORT_HOST}/planifrepas/plat")
        for i in response.json():
            listItem.append(i)
        return render_template("plat.html",data =listItem, len = len(listItem))
    
    @app.route('/entree')
    def displayEntree():
        listItem=[]
        response = requests.get(f"http://{RANDOM_HOST}:{PORT_HOST}/planifrepas/entree")
        for i in response.json():
            listItem.append(i)
        return render_template("plat.html",data =listItem, len = len(listItem))
    
    @app.route('/displayRecipe/<int:id>')
    def displayRecipe(id):
        listItem=[]
        response = requests.get(f"http://{RANDOM_HOST}:{PORT_HOST}/planifrepas/displayRecipe/{id}")
        for i in response.json():
            listItem.append(i)
        return render_template("displayRecipe.html",data =response.json())
    #Routes random meal####################################################################################
    @app.route('/accueil')
    def accueil():
        return render_template("accueil.html")
    
    
    @app.route('/sign-up',  methods=['GET', 'POST'])
    def sign_up():
        if request.method == 'POST':
            email = request.form.get('email')
            first_name = request.form.get('nom')
            password1 = request.form.get('pwd')
            password2 = request.form.get('pwd')

            user = db.session.query(db.User).filter(db.User.email==email).first()
            if user:
                flash('Email already exists.')
            elif len(email) < 4:
                flash('Email must be greater than 3 characters.')
            elif len(first_name) < 2:
                flash('First name must be greater than 1 character.')
            elif password1 != password2:
                flash('Passwords don\'t match.')
            elif len(password1) < 7:
                flash('Password must be at least 7 characters.')
            else:
                stmt = (
                    insert(db.User).                    
                    values(id=random.randint(5, 100), email=email, first_name=first_name, password=generate_password_hash(
                     password1, method='sha256') )
                    )
                db.engine.execute(stmt)
                db.session.commit()
         
                # flash('Account created!')
                return redirect(url_for('login'))

        return render_template("inscription.html", user=current_user)

    @app.route('/flash')
    def flash():
        message = request.args.get("msg")
        return render_template("flash.html", msg=message)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

if __name__ == '__main__':
    app= create_app()
    app.run(host=SERVER_HOST, port=int(SERVER_PORT), debug=bool(DEBUG_MODE))

