from flask import Flask, render_template, request
from model.user import User
from controller.usercontroller import userController


app = Flask(__name__)
user=User()
usercontroller = userController()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/connexion")
def connexion():
    pass

@app.route("/accueil")
def accueil():
    return render_template("accueil.html")

@app.route("/profil")
def profil():
    return render_template("profil.html")

@app.route("/abonnement")
def abonnement():
    return render_template("abonnement.html")

@app.route("/paiement")
def paiement():
    return render_template("paiement.html")

#---------------------------------CRUD USER------------------------------#
@app.route("/inscription")
def addUser():
    return usercontroller.create()


@app.route("/traitementUser", methods=['POST', 'GET'])
def traitementUser():
    data=request.form
    return usercontroller.treateCreate(user,data)