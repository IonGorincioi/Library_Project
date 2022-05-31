
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


#  Create a Flask instance
app = Flask(__name__)

#  configure the secret key
app.config['SECRET_KEY'] = 'mysecretkey'

###############  DATABASE SETUP  ################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()                 #   create an instance of LoginManager

db = SQLAlchemy(app)            #  Create a database object 
Migrate(db, app)                #  Connect the app with database

################################################

############  LOGIN CONFIGURATION SETUP  ###########

login_manager.init_app(app)                    #   Pass in the app to the login_manager
login_manager.login_view = 'users.login'       #   tell the users what view to go to when they need to log in

###################################################


###################################################
###########  BLUEPRINTS REGISTRATION  #############
###################################################

from libraryProjectContent.core.views import core
from libraryProjectContent.users.views import user
from libraryProjectContent.admin.views import administrator
from libraryProjectContent.books.views import book


app.register_blueprint(core)
app.register_blueprint(user, url_prefix='/users')
app.register_blueprint(administrator, url_prefix='/admin')
app.register_blueprint(book, url_prefix='/books')