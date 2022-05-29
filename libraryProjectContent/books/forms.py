from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired

class AddBook(FlaskForm):
    id = IntegerField('ID')
    ISBN = StringField('ISBN', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    publisher = StringField('Publisher')
    description = TextAreaField ('Description')
    add = SubmitField('Add')
    update = SubmitField('Update')
    delete = SubmitField('Delete')


