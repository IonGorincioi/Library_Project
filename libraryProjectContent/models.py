########################################################
################### MODELS.PY ##########################
########################################################
from enum import unique
from libraryProjectContent import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin                     #  UserMixin allows us to have functionality such as "Is_Authenticated", "is_Active" etc. 
from libraryProjectContent.admin.views import index     

#   next function will allow isers to log in, taking the user id,
#   returning the user_id provided from the database
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


########################################################
###################  SET UP ADMIN CLASS   ###############
########################################################
class Admin(db.Model, UserMixin):
    __tablename__='administrators'
    id = db.Column(db.Integer, primary_key=True)
    fName = db.Column(db.String())
    lName = db.Column(db.String())
    username = db.Column(db.String(), unique=True, index=True)
    email = db.Column(db.String(), unique=True, index=True)
    password = db.Column(db.String())


#  Define the __init__ method to be able to create admin objects
    def __init__(self, fName, lName, username, email, password):
        self.fName = fName
        self.lName = lName
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


##  Create another method that will check if the password provided during login
    def check_password(self, password):
        return check_password_hash(self.password, password)


##   Create a method that will return a string representation of administrator
    def __repr__(self):
        return f"Username {self.username}"


########################################################
###################  SET UP USER CLASS   ###############
########################################################

class User(db.Model, UserMixin):
    __tablename__ ='users'

    id = db.Column(db.Integer, primary_key = True )
    fName = db.Column(db.String(64))
    lName = db.Column(db.String(64))
    username = db.Column(db.String(64), unique = True, index=True)
    email = db.Column(db.String(64), unique = True, index=True)
    password_hash = db.Column(db.String(128))
    
##  Create an __init__ method to be able to create an instance of the user later on
    def __init__(self, fName, lName, username, email, password):
        self.fName = fName
        self.lName = lName
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

##  Create another method that will check if the password provided during login
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

##   Create a method that will return a string representation of a user

    def __repr__(self):
        return f"Username {self.username}"

########################################################
###################  SET UP BOOK CLASS   ###############
########################################################

class Book(db.Model):

    __tablename__= 'books'
    # users = db.relationship(User)

    id = db.Column(db.Integer, primary_key = True)
    ISBN = db.Column(db.String(), unique=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    publisher = db.Column(db.String)
    description = db.Column(db.Text)

    def __init__(self, id, ISBN, title, author, publisher, description):
        self.id = id
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.publisher = publisher
        self.description = description

    def __repr__(self):
        return f"{self.id} {self.ISBN} {self.title} {self.author} {self.publisher} {self.description}"


