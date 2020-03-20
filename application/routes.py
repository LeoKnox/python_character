from application import app, db
from flask import render_template, request

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
    #Character(char_id=1, char_name="Eveehi", char_class="Paladin", char_atk=7, char_def=11, char_hp=23).save()
    #Character(char_id=2, char_name="Ynzon", char_class="Rogue", char_atk=9, char_def=14, char_hp=15).save()
    chars = Character.objects.all()
    return render_template("character.html", chars=chars, character="active")

@app.route("/spells")
def spells():
    spellData = [{"spellID":"1111","title":"Fireball","casting":8,"type":"fire"},
        {"spellID":"1112","title":"Stunning Touch","casting":6,"type":"lightning"},
        {"spellID":"1113","title":"Snow Ball","casting":3,"type":"ice"},
        {"spellID":"1114","title":"Summon Demon","casting":4,"type":"demon"}]
    return render_template("spells.html", spellData=spellData, spells="active")

@app.route("/selection", methods=["Get", "POST"])
def selection():
    id = request.form.get('spellID')
    title = request.form.get('title')
    spell_type = request.form.get('type').capitalize()
    return render_template("selection.html", login="active", data={ "id":id, "title":title, "type":spell_type })

@app.route("/login")
def login():
    return render_template("login.html", login="active")