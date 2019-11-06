#nakodovani na filtraci
#importuju knihovnu pro práci s PostgreSQL
import psycopg2
import psycopg2.extras
#knihovna na interakci s generačním systémem
import os

#funkce pro spojení s databázemi

def get_db():
    url = os.getenv('DATABASE_URL')
    conn = psycopg2.connect(url, sslmode='require', cursor_factory=psycopg2.extras.NamedTupleCursor)
    return conn 

def get_lectureType():
    sql = """SELECT lesson FROM prehled GROUP BY lesson ORDER BY lesson ASC"""
    conn = get_db()
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return data

def insert_classes (lesson, teacher, studio, day, time_from, time_to, age_group, level, course_type, address, address_city, link, email_address): 
    sql = """INSERT INTO prehled(school, \"ageGroupFrom\", \"ageGroupTo\", level, lecturer, lesson, type, day, time, link, address, \"PSC\", city_part, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"""
    t = time_from.strftime("%H:%M")+" - "+time_to.strftime("%H:%M")
    conn = get_db()
    cur = conn.cursor()
    cur.execute(sql, (studio, None, None, level, teacher, lesson, course_type, day, t, link, address, None, address_city, None, None))
    data = cur.fetchone()[0]
    conn.commit()
    return data

def get_studioType():
    sql = """SELECT school FROM prehled GROUP BY school"""
    conn = get_db()
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return data

def get_cityType():
    sql = """SELECT city_part FROM prehled GROUP BY city_part"""
    conn = get_db()
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return data

def get_search(city_part, age, school, lesson, monday, tuesday, wednesday, thursday, friday, saturday, sunday):
    sql = """ SELECT * FROM prehled WHERE id IS NOT NULL""" 
    parameters = []
    if city_part:
        command = " AND \"city_part\" = %s"
        parameters += [city_part]
        sql=sql + command
    if age:
        command = " AND \"ageGroupFrom\" <= %s AND \"ageGroupTo\" >= %s"
        parameters += [age,age]
        sql=sql + command
    if school:
        command = " AND \"school\" = %s"
        parameters += [school]
        sql=sql + command
    if lesson:
        command = " AND \"lesson\" = %s"
        parameters += [lesson]
        sql=sql + command
    days = []
    if monday:
        days.append("\"day\" = %s")
        parameters += ["Pondělí"]
    if tuesday:
        days.append("\"day\" = %s")
        parameters += ["Úterý"]
    if wednesday:
        days.append("\"day\" = %s")
        parameters += ["Středa"]
    if thursday:
        days.append("\"day\" = %s")
        parameters += ["Čtvrtek"]
    if friday:
        days.append("\"day\" = %s")
        parameters += ["Pátek"]
    if saturday:
        days.append("\"day\" = %s")
        parameters += ["Sobota"]
    if sunday:
        days.append("\"day\" = %s")
        parameters += ["Neděle"]
    if days:
        command = " AND (" + " OR ".join(days) + ")"
        sql=sql + command
    
    
    conn = get_db()
    cur = conn.cursor()
    cur.execute(sql, parameters)
    data = cur.fetchall()
    return data

