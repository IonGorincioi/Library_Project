from flask import render_template,Blueprint, url_for, redirect, flash
from libraryProjectContent.admin.forms import  LoginAdmin


administrator = Blueprint('admin', __name__) 


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
@administrator.route('/loginAdm', methods=['GET', 'POST'])
def adminlogin():
   
    form = LoginAdmin()  
    print('form', form)                              #  Create an instance for the form from "LoginForm" object
    if form.validate_on_submit():

        flash("You've been logged in successfuly as Administrator!")
        return redirect(url_for('admin.index'))
    return render_template('adminlogin.html', form=form)



  