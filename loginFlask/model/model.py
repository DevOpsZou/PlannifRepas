
from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for, jsonify
from sqlalchemy import insert
from flask_sqlalchemy import SQLAlchemy

class Model():
    
    def __init__(self, db):
        self._db=db
    
    def getUserByEmail(self, email):
        self.user=self._db.session.query(self._db.User).filter(self._db.User.email==email).first()
        return self.user