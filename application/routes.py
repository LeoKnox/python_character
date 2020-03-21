from application import app, db
from flask import render_template, request, redirect, flash
from application.models import Character, Spell, SpellBook
from application.forms import LoginForm, CreateForm

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

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.form.get("char_name") == "Aelien":
            flash("You are logged in.")
            return redirect("/index")
        else:
            flash("Error try again.")
    return render_template("login.html", form=form, login="active")