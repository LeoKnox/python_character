from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", home="active")

@app.route("/create")
def create():
    return render_template("create.html", home="active")

@app.route("/character")
def character():
    return render_template("character.html", home="active")

@app.route("/login")
def login():
    return render_template("login.html", home="active")