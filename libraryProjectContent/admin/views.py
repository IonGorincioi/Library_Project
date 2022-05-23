from flask import render_template,Blueprint, url_for, redirect, session, flash
from libraryProjectContent.admin.forms import  LoginAdmin


administrator = Blueprint('admin', __name__, 
                           template_folder = 'templates/admin')     #   assign a template folder that flask should look for  templates


#########################################################
#############    SET UP THE LOGOUT VIEW    ##############
#########################################################
@administrator.route('/logout')
def logout():

    return render_template('logout.html')

#########################################################
#############    SET UP THE INDEX VIEW    ##############
#########################################################

@administrator.route('/index')
def index():
    return render_template('admin_index.html')

    

#########################################################
#############    SET UP THE LOGIN VIEW    ##############
#########################################################
@administrator.route('/login', methods=['GET', 'POST'])
def adminlogin():
   
    admform = LoginAdmin()                               #  Create an instance for the form from "LoginForm" object
    if admform.validate_on_submit():
        session['username'] = admform.username.data
        flash(f"Hi {session['username']}. You've been logged in as Administrator successfully!")
        return redirect(url_for('admin.index'))
    return render_template('adminlogin.html', admform=admform)



  