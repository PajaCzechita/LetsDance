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

def insert_classes (lesson, teacher, studio, day, time_from, time_to, age_group, level, course_type, address, address_city, link, email_address): 
    sql = """INSERT INTO prehled(school, ageGroupFrom, ageGroupTo, level, lecturer, lesson, type, day, time, link, address, PSC, city_part, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    t = time_from.strftime("%H:%M")+" - "+time_to.strftime("%H:%M")
    conn = get_db()
    cur = conn.cursor()
    cur.execute(sql, (studio, None, None, level, teacher, lesson, course_type, day, t, link, address, None, address_city, None, None))
    data = cur.fetchone()[0]
    return data

