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
    sql = """SELECT lesson FROM prehled GROUP BY lesson"""
    conn = get_db()
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
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

def get_search(city_part, age, lesson, day):
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
    if lesson:
        command = " AND \"lesson\" = %s"
        parameters += [lesson]
        sql=sql + command
    if day:
        command = " AND \"day\" = %s"
        parameters += [day]
        sql=sql + command
    conn = get_db()
    cur = conn.cursor()
    cur.execute(sql, parameters)
    data = cur.fetchall()
    return data

