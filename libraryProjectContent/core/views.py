from flask import render_template, Blueprint, request

core: Blueprint = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/about')
def info():
    return render_template('info.html')