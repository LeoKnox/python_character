from application import app
from flask import render_template, request, redirect, flash, url_for, session

@app.route('/dungeon')
def dungeon():
    room = {"length":15, "width":15}
    player = {"locx":3, "locy":5}
    return render_template("dungeon.html", room=room, player=player)