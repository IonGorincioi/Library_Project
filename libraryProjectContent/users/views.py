# register
# login
# logout
# account (update userform)
# users list of books

#  Import necessary files
from flask import render_template, Blueprint, redirect, flash, url_for, session, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from libraryProjectContent.users.forms import LoginForm, RegistrationForm, UpdateUserForm
from libraryProjectContent import db
from libraryProjectContent.models import User

#  Create the "user" instance from the Blueprint class
user = Blueprint('users', __name__,
                  template_folder='templates/users')


#########################################################
#############    SET UP THE LOGOUT VIEW    ##############
#########################################################
@user.route('/logout')
@login_required
def logout():
    logout_user()                           #  logout_user function imported from flask_login
    flash("You've been logged out! ")
    return render_template(url_for('core.index'))

##############################################################
##################  SET UP THE LOGIN VIEW ####################
##############################################################
@user.route('/login', methods=['GET', 'POST'])
def login():
    
    userform = LoginForm()                                   #  Create an instance for the form from "LoginForm" object    
    if userform.validate_on_submit():
        user = User.query.filter_by(username=userform.username.data).first()
        
        if user.check_password(userform.password.data)and user is not None:
            login_user(user)
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
    # session['name'] = userform.firstName.data
    if userform.validate_on_submit():                          #  if the submit was clicked
       
       #  create an user object
        user = User(fName=userform.firstName.data,
                    lName=userform.lastName.data,
                    email=userform.email.data,
                    username=userform.username.data,
                    password=userform.password.data)

        #  grab the session of database and add in the created user
        db.session.add(user)      
        db.session.commit()

        #  flash a message and redirect to user login page
        flash(f"Congratulations {session['name']}! You've been registered as a user. In order to access your account please log in")
        return redirect(url_for('users.login'))  

    return render_template('user_register.html',userform=userform)

##############################################################
#############  SET UP THE THANKYOU VIEW ######################
##############################################################      
@user.route('/thankyou')
def thankyou():
    
    return render_template('thankyou.html')


##############################################################
#############  SET UP THE UPDATE VIEW ######################
##############################################################
@user.route('/update', methods = ['GET','POST'])

def updateUser():

    updtform = UpdateUserForm()

    if updtform.validate_on_submit():
        user = User(fName=updtform.firstName.data,
                    lName=updtform.lastName.data,
                    email = updtform.email.data,
                    username = updtform.username.data)
        
        db.session.update(user)
        db.session.commit()

        flash('Your "username" and "email" has been updated')
        return redirect(url_for('users.updateUser'))

    return render_template('update.html', userform = updtform)




    