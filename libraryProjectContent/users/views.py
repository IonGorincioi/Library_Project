#  Import necessary files

from distutils.command.build_scripts import first_line_re
from flask import render_template, Blueprint, redirect, flash, url_for
from libraryProjectContent.admin.forms import LoginAdmin
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
    
    form = LoginForm()                                   #  Create an instance for the form from "LoginForm" object    
    if form.validate_on_submit():
        
        flash('Log in Successfully as a user!')
        return redirect(url_for('core.index'))
        
    return render_template('login.html', form=form)


##############################################################
#############  SET UP THE REGISTRATION VIEW ##################
##############################################################
@user.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()                           #  Create an Instance from "RegistrationForm" object 
                                                        #  that was created in "forms.py" file
    
    if form.validate_on_submit():                          #  if the submit was clicked
        
        flash("Congratulations! You've been registered as a user.In order to access your account please log in")
        return redirect(url_for('users.login'))         #  Redirect the user to the login page

    return render_template('register.html',form=form)

##############################################################
#############  SET UP THE thankyou VIEW ##################
##############################################################      
@user.route('/thankyou')
def thankyou():
    
    return render_template('thankyou.html')
    


