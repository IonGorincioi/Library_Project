#  Import necessary files


from flask import render_template, Blueprint, redirect, flash, url_for, session
from libraryProjectContent.users.forms import LoginForm, RegistrationForm

#  Create the "user" instance from the Blueprint class
user = Blueprint('users', __name__,
                  template_folder='templates/users')


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
        flash(f" You have been logged in as {session['username']}")
        return redirect(url_for('core.index'))
        
    return render_template('user_login.html', userform=userform)

  
##############################################################
#############  SET UP THE REGISTRATION VIEW ##################
##############################################################
@user.route('/register', methods=['GET', 'POST'])
def register():

    userform = RegistrationForm()                              #  Create an Instance from "RegistrationForm" object 
                                                               #  that was created in "forms.py" file
    session['name'] = userform.firstName.data
    if userform.validate_on_submit():                          #  if the submit was clicked
        
        flash(f"Congratulations {session['name']}! You've been registered as a user. In order to access your account please log in")
        return redirect(url_for('users.login'))         #  Redirect the user to the login page

    return render_template('user_register.html',userform=userform)

##############################################################
#############  SET UP THE thankyou VIEW ##################
##############################################################      
@user.route('/thankyou')
def thankyou():
    
    return render_template('thankyou.html')
    


