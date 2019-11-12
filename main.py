from flask import Flask, render_template, redirect, url_for, request
import db_functions
from forms.registration import RegistrationForm

application = Flask('letsdance') 

@application.route('/formular')
def show_formular():
    return render_template('formular.html', type=db_functions.get_lectureType(), studio=db_functions.get_studioType(),
                           city=db_functions.get_cityType(), search=[], results=False)

@application.route('/hledani', methods=['POST'])
def submit_formular():
    city = request.form['city']
    vek = request.form['vek']
    studio = request.form['studio']
    pondeli = request.form.get('Den_Pondeli')
    utery = request.form.get('Den_Utery')
    streda = request.form.get('Den_Streda')
    ctvrtek = request.form.get('Den_Ctvrtek')
    patek = request.form.get('Den_Patek')
    sobota = request.form.get('Den_Sobota')
    nedele = request.form.get('Den_Nedele')
    lekce = request.form['lekce']
    return render_template('vysledky_vyhledavani.html', search=db_functions.get_search(city, vek, studio, lekce, pondeli, utery, streda, ctvrtek, patek, sobota, nedele), results=True)

@application.route('/seznam')
def get_lesson():
    expectation_table = db_functions.get_studios()
    #print(expectation_table)
    return render_template("list.html",
    expectation_table=expectation_table
    )


@application.route('/')
def show_index():
    return render_template('index.html')

@application.route('/about')
def show_about():
    return render_template('about.html')
    
@application.route('/registrace', methods = ['POST', 'GET'])
def add_course():
    form = RegistrationForm(csrf_enabled = False)
    if form.validate_on_submit(): 
        id = db_functions.insert_classes(
          form.lesson.data, 
          form.lecturer.data, 
          form.studio.data, 
          form.day.data, 
          form.time_from.data,
          form.time_to.data,
          form.age_group.data,
          form.level.data,
          form.course_type.data,
          form.address.data,
          form.address_city.data,
          form.link.data,
          form.email_address.data,
          )
        print("Inserted row as ID " + str(id))
        return redirect (url_for ("seznam"))
    return render_template('registrace.html', form = form)
