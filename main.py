from flask import Flask, render_template, request
from db_functions import get_lectureType
from db_functions import get_studioType
from db_functions import get_cityType
from db_functions import get_search

application = Flask('letsdance') 

@application.route('/formular')
def show_formular():
    return render_template('formular.html', type=get_lectureType(), studio=get_studioType(), city=get_cityType(), search=[])

@application.route('/hledani', methods=['POST'])
def submit_formular():
    city = request.form['city']
    vek = request.form['vek']
    studio = request.form['studio']
    den = request.form['den']
    lekce = request.form['lekce']
    return render_template('formular.html', type=get_lectureType(), studio=get_studioType(), city=get_cityType(), search=get_search(city, vek, lekce, den))

@application.route('/')
def show_layout():
    return render_template('layout.html')
    

