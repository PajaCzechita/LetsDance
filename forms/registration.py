from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, DataRequired, Email
from wtforms_components import TimeField

class RegistrationForm(FlaskForm): 
    lesson = StringField ("Název lekce", validators = [InputRequired(message = "Napiš název lekce - typ tance.")])
    lecturer = StringField ("Lektor", validators = [InputRequired(message = "Zadej jméno lektora, nevedené sessions tady nehledáme. ;-)")])
    studio = StringField ("Taneční studio", validators = [InputRequired(message = "Pokud lekce není venku, napiš prosím Tě název studia. ;-)")])
    day = SelectField ("Den", choices = [("Monday", "Pondělí"), ("Tuesday", "Úterý"),("Wednesday", "Středa"),("Thursday", "Čtvrtek"),("Friday", "Pátek"),("Saturday", "Sobota"),("Sunday", "Neděle")])
    time_from = TimeField ("Čas lekce od", validators = [InputRequired(message = "Zadej, v kolik hodin lekce začíná.")])
    time_to = TimeField ("Čas lekce do", validators = [InputRequired(message = "Nic netrvá věčně, zadej, v kolik hodin lekce končí. ;-)")])
    age_group = RadioField ("Pro", choices = [("adults", "Dospělé"), ("children", "Děti")])
    level = SelectField ("Náročnost", choices = [("Beginners", "Začátečníci"), ("PreIntermediate", "Mírně pokročilí"),("Intermediate", "Pokročilí"),("AllLevels", "All Levels")])
    course_type = SelectField ("Typ lekce", choices = [("Openclass", "Open Class"), ("Course", "Kurz")])
    address = StringField ("Ulice a č.p.", validators = [InputRequired(message = "Vložte pouze ulici a číslo popisné / orientační.")])
    address_city = SelectField ("Vyber obvod Prahy", choices = [("P1", "Praha 1"), ("P2", "Praha 2"),("P3", "Praha 3"),("P4", "Praha 4"),("P5", "Praha 5"),("P6", "Praha 6"),("P7", "Praha 7"), ("P8", "Praha 8"), ("P9", "Praha 9"),("P10", "Praha 10")])
     #fce get gps, aby nám to dohledalo souřadnic
    link = StringField ("Link na kurz/lekci", validators = [InputRequired(message = "Vlož odkaz na lekci / kurz / rozvrh.")])
    email_address = StringField ("E-mailová adresa vkladatele", validators = [DataRequired(message = "Napiš svou kontaktní e-mailovou adresu."), Email(message = "Takhle by Ti email nepřišel, oprav si to prosím."), Length (min=4, max = 100)])
