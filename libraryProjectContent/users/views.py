#  Import necessary files

from distutils.command.build_scripts import first_line_re
from flask import render_template, Blueprint, redirect, flash, url_for, session
from libraryProjectContent.users.forms import LoginForm, RegistrationForm

#  Create the "user" instance from the Blueprint class
user = Blueprint('users', __name__)



#########################################################
#############    SET UP THE LOGOUT VIEW    ##############
#########################################################
@user.route('/logout')
def logout():

    return render_template('logout.html')



##############################################################
##################  SET UP THE LOGIN VIEW ####################
##############################################################
@user.route('/login', methods=['GET', 'POST'])
def login():
    
    userform = LoginForm()                                   #  Create an instance for the form from "LoginForm" object    
    if userform.validate_on_submit():
        session['username'] = userform.username.data
        flash(f"Hello {session['username']}. You have logged in Successfully as a user!")
        return redirect(url_for('core.index'))
        
    return render_template('login.html', userform=userform)


##############################################################
#############  SET UP THE REGISTRATION VIEW ##################
##############################################################
@user.route('/register', methods=['GET', 'POST'])
def register():

    userform = RegistrationForm()                           #  Create an Instance from "RegistrationForm" object 
                                                        #  that was created in "forms.py" file
    session['name'] = userform.username.data
    if userform.validate_on_submit():                          #  if the submit was clicked
        
        flash(f"Congratulations {session['username']}! You've been registered as a user. In order to access your account please log in")
        return redirect(url_for('users.login'))         #  Redirect the user to the login page

    return render_template('register.html',userform=userform)

##############################################################
#############  SET UP THE thankyou VIEW ##################
##############################################################      
@user.route('/thankyou')
def thankyou():
    
    return render_template('thankyou.html')
    


