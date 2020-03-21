import flask
from application import db

class Character(db.Document):
    char_id         =   db.IntField( unique=True )
    char_name       =   db.StringField( max_length=50 )
    char_class      =   db.StringField( max_length=30 )
    char_atk        =   db.IntField()
    char_def        =   db.IntField()
    char_hp         =   db.IntField()

class Spell(db.Document):
    spellID     =   db.StringField(max_length=10, unique=True )
    title       =   db.StringField( max_length=30 )
    casting     =   db.IntField()
    spell_type  =   db.StringField( max_length=30 )

class SpellBook(db.Document):
    char_id         =   db.IntField()
    spellID         =   db.StringField( max_length=10 )