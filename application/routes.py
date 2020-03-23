from application import app, db
from flask import render_template, request, redirect, flash, url_for, session
from application.models import Character, Spell, SpellBook
from application.forms import LoginForm, CreateForm

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", home="active")

@app.route("/create", methods=["GET", "POST"])
def create():
    if session.get('charname'):
        return redirect(url_for('index'))

    form = CreateForm()
    if form.validate_on_submit():
        char_id     =   Character.objects.count()
        char_id     +=1

        char_name   =   form.char_name.data
        char_class  =   form.char_class.data
        char_atk    =   form.char_atk.data
        char_def    =   form.char_def.data
        char_hp     =   form.char_hp.data

        char = Character(char_id=char_id, char_name=char_name, char_class=char_class, char_atk=char_atk, char_def=char_def, char_hp=char_hp)
        char.save()
        return redirect(url_for('index'))

    return render_template("create.html", create="active", form=form)

@app.route("/character")
def character():
    chars = Character.objects.all()
    return render_template("character.html", chars=chars, character="active")

@app.route("/spells")
def spells():
    spellData = Spell.objects.all()
    return render_template("spells.html", spellData=spellData, spells="active")

@app.route("/selection", methods=["Get", "POST"])
def selection():
    if not session.get('charname'):
        return redirect(url_for('login'))

    spellID = request.form.get('spellID')
    title = request.form.get('title')
    char_id = session.get('char_id')

    if spellID:
        if SpellBook.objects(char_id=char_id,spellID=spellID):
            flash(f'{title} already in book')
            return redirect(url_for("spells"))
        else:
            SpellBook(char_id=char_id, spellID=spellID)
            flash(f'{title} added to spellbook')
    spells = list( Character.objects.aggregate(*[
        {
            '$lookup': {
                'from': 'spellbook', 
                'localField': 'char_id', 
                'foreignField': 'char_id', 
                'as': 'r1'
            }
        }, {
            '$unwind': {
                'path': '$r1', 
                'includeArrayIndex': 'r1_id', 
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$lookup': {
                'from': 'spell', 
                'localField': 'r1.spellID', 
                'foreignField': 'spellID', 
                'as': 'r2'
            }
        }, {
            '$unwind': {
                'path': '$r2', 
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$match': {
                'char_id': char_id
            }
        }, {
            '$sort': {
                'spellID': 1
            }
        }
    ]))
    return render_template("selection.html", selection="active", spells=spells)

@app.route("/login", methods=['GET','POST'])
def login():
    if session.get('charname'):
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        char_name = form.char_name.data
        char = Character.objects(char_name=char_name).first()
        if char and char_name == char.char_name:
            flash("You are logged in.")
            session['charname'] = char.char_name
            session['char_id'] = char.char_id
            return redirect("/index")
        else:
            flash("Error try again.")
    return render_template("login.html", form=form, login="active")

@app.route("/logout")
def logout():
    session['charname']=False
    session['char_id']=False
    return redirect(url_for('index'))