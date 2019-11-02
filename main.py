from flask import Flask, render_template
from db_functions import get_lectureType
application = Flask('letsdance') 

@application.route('/')
def show_layout():
    return render_template('layout.html')
    

@application.route('/formular')
def show_formular():
    return render_template('formular.html', type=get_lectureType())