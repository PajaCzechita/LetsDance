from flask import Flask, render_template
application = Flask('letsdance') 

@application.route('/')
def show_index():
    return render_template('index.html')
    