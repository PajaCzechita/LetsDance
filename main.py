from flask import Flask, render_template, redirect, url_for, request
import db_functions
from forms.registration import RegistrationForm

application = Flask('letsdance') 

@application.route('/formular')
def show_formular():
    return render_template('formular.html', type=db_functions.get_lectureType(), studio=db_functions.get_studioType(),
                           city=db_functions.get_cityType(), search=[])

@application.route('/hledani', methods=['POST'])
def submit_formular():
    city = request.form['city']
    vek = request.form['vek']
    studio = request.form['studio']
    den = request.form['den']
    lekce = request.form['lekce']
    return render_template('formular.html', type=db_functions.get_lectureType(), studio=db_functions.get_studioType(), 
                           city=db_functions.get_cityType(), search=db_functions.get_search(city, vek, lekce, den))

@application.route('/')
def show_layout():
    return render_template('layout.html')
 
@application.route('/formular')
def show_formular():
    return render_template('formular.html', type=db_functions.get_lectureType())

@application.route('/registrace', methods = ['POST', 'GET'])
def add_course():
    form = RegistrationForm(csrf_enabled = False)
    if form.validate_on_submit(): 
        db_functions.insert_classes(
          form.lesson.data, 
          form.lecturer.data, 
          form.studio.data, 
          form.day.data, 
          form.time_from.data,
          form.time_to,
          form.age_group.data,
          form.level.data,
          form.course_type.data,
          form.address.data,
          form.address_city.data,
          form.link.data,
          form.email_address.data,
          )
        return redirect (url_for ("show_formular"))
    return render_template('registrace.html', form = form)

