from application import app
from flask import render_template, request, redirect, flash, url_for, session

@app.route('/dungeon')
def dungeon():
    return render_template("dungeon.html")