# -*- encoding: utf-8 -*-
"""
Light Bootstrap Dashboard - coded in Flask

Author  : AppSeed App Generator
Design  : Creative-Tim.com
License : MIT 
Support : https://appseed.us/support 
"""

from app         import db
from flask_login import UserMixin

class User(UserMixin, db.Model):

    id       = db.Column(db.Integer,     primary_key=True)
    user     = db.Column(db.String(64),  unique = True)
    email    = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(500))
    # energy figures
    today_energy = db.Column(db.Integer)
    week_energy = db.Column(db.Integer)
    month_energy = db.Column(db.Integer)

    # driving figures
    week_drive = db.Column(db.Integer)
    month_drive = db.Column(db.Integer)
    year_drive = db.Column(db.Integer)

    # public transport figures

    week_pt = db.Column(db.Integer)
    month_pt = db.Column(db.Integer)
    year_pt = db.Column(db.Integer)
    
    # eat out figures

    week_eat = db.Column(db.Integer)
    month_eat = db.Column(db.Integer)
    year_eat = db.Column(db.Integer)

    




    def __init__(self, user, email, password):
        self.user       = user
        self.password   = password
        self.email      = email

    def __repr__(self):
        return '<User %r>' % (self.id)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 
