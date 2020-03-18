from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", home="active")

@app.route("/create")
def create():
    return render_template("create.html", create="active")

@app.route("/character")
def character():
    return render_template("character.html", character="active")

@app.route("/spells")
def spells():
    spellData = [{"spellID":"1111","title":"Fireball","casting":8,"type":"fire"},
        {"spellID":"1112","title":"Stunning Touch","casting":6,"type":"lightning"},
        {"spellID":"1113","title":"Snow Ball","casting":3,"type":"ice"},
        {"spellID":"1114","title":"Summon Demon","casting":4,"type":"demon"}]
    return render_template("spells.html", spellData=spellData, spells="active")

@app.route("/login")
def login():
    return render_template("login.html", login="active")