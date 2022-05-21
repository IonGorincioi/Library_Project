
# # Form imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

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
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username')
    password =  PasswordField('Password')
    pass_confirm =  PasswordField('Confirm password')
    submit = SubmitField('Register')


############################################################
############   CREATE THE UPDATE THE USER FORM   ###########
############################################################

# class UpdateUserForm(FlaskForm):


