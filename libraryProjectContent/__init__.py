from flask import Flask

app = Flask(__name__)

#  configure the secret key
app.config['SECRET_KEY'] = 'mysecretkey'

from libraryProjectContent.core.views import core
from libraryProjectContent.users.views import user
from libraryProjectContent.admin.views import administrator


app.register_blueprint(core)
app.register_blueprint(user)
app.register_blueprint(administrator)