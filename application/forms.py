from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError

class LoginForm(FlaskForm):
    char_name   =   StringField("Character Name", validators=[DataRequired()])
    char_class  =   StringField("Character Class", validators=[DataRequired()])
    remember_me =   BooleanField("Remember Me")
    submit      =   SubmitField("Login")

class CreateForm(FlaskForm):
    char_name   =   StringField("Character Name", validators=[DataRequired()])
    char_class  =   StringField("Class", validators=[DataRequired()])
    #confirm_class = StringField("Confirm Class", validators=[DataRequired()])
    char_atk    =   IntegerField("Attack", validators=[DataRequired()])
    char_def    =   IntegerField("Defense", validators=[DataRequired()])
    char_hp     =   IntegerField("Hit Points", validators=[DataRequired()])
    submit      =   SubmitField("Create Now")

    def vaildate_name(self, char_name):
        char = Character.objects(char_name=char_name.data).first()
        if user:
            raise ValidationError("Name is use, choose another.")