
# # Form imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileAllowed, FileField
from libraryProjectContent.models import User


# ############################################################
# #############   CREATE THE LOGIN FORM   #############
# ############################################################

class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Log in')


# ############################################################
# #############   CREATE THE REGISTRATION FORM   #############
# ############################################################

class RegistrationForm(FlaskForm):
    firstName = StringField('First name', validators=[DataRequired()])
    lastName = StringField('Surname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password =  PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match!0')])
    pass_confirm =  PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    ##  Check if the the email and username hasn't been already taken
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email has been already registered.')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username has been already taken.')



############################################################
############   CREATE THE UPDATE THE USER FORM   ###########
############################################################

##  This form will allow users to change their login credentials if they want to
class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Update')

    ##  Next functions will make sure thet the user will nor enter an email
    ##  and a username that has been already used
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email has been already registered.')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username has been already taken.')
