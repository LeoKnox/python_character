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

@app.route("/login")
def login():
    return render_template("login.html", login="active")