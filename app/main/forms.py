from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, Length


# User Forms
class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class EditProfileForm(Form):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

