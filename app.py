from bottle import route, template, run, request, redirect
import pymysql
import os

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2608993339', passwd='mypassword', db='2608993339_vefth_bilar')
c = conn.cursor()

c.execute('SELECT * FROM bilar WHERE skraningarnumer ="AB-123"')
records = c.fetchall()

#c.execute('INSERT INTO bilar Values("BA-456", "Toyota Corolla(Grænn)","XXXXXX" ,"2016-01-01","50",1200,"2020-01-01","Í umferð")')
#conn.commit()

#c.execute('DELETE FROM bilar where skraningarnumer = "BA-456"')
#conn.commit()

#c.execute('UPDATE bilar SET stada = "Í umferð" where skraningarnumer = "AB- 123"')
#conn.commit()

conn.close()
c.close()

print(records)

@route('/')
def index():
    return template('index')

@route('/car_info')
def car_info():
    nr = request.query.get('leit')
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2608993339', passwd='mypassword', db='2608993339_vefth_bilar')
    c = conn.cursor()

    c.execute('SELECT * FROM bilar WHERE skraningarnumer = %s', (nr))
    bill = c.fetchone()

    conn.close()
    c.close()

    if bill:
        return template('car_info', bill=bill)
    else:
        return 'Skráningarnúmer ekki í grunni. <br>'\
                '<a href="/">Til baka</a>'

@route('/db/add')
def add_to_db():
    return template('newcar')

@route('/db/add', method='POST')
def submit_record():
    skr_nr = request.forms.get('skr_nr')
    tegund = request.forms.tegund
    vrk_nr = request.forms.get('vrk_nr')
    skr_dags = request.forms.get('skr_dags')
    co2 = request.forms.get('co2')
    tyngd = request.forms.get('tyngd')
    sko_dags = request.forms.get('sko_dags')
    stada = request.forms.stada

    co2 = int(co2)
    tyngd = int(tyngd)

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2608993339', passwd='mypassword', db='2608993339_vefth_bilar')
    c = conn.cursor()

    c.execute('SELECT * FROM bilar')
    records = c.fetchall()

    if any(skr_nr in r for r in records):
        conn.close()
        c.close()
        return 'Skráningarnúmer þegar til.'\
                '<br><a href="/>Til baka.</a>'
    else:
        c.execute("INSERT INTO bilar Values('{}','{}','{}','{}','{:d}','{:d}','{}','{}')".format(skr_nr, tegund, vrk_nr, skr_dags, co2, tyngd, sko_dags, stada))
        conn.commit()

        conn.close()
        c.close()
        return redirect('/')

@route('/db/del/<nr>')
def del_from_db(nr):
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2608993339', passwd='mypassword', db='2608993339_vefth_bilar')
    c = conn.cursor()

    c.execute('DELETE FROM bilar where skraningarnumer = %s', (nr))
    conn.commit()

    conn.close()
    c.close()

    return redirect('/')

@route('/db/update/<nr>')
def update_db(nr):
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2608993339', passwd='mypassword', db='2608993339_vefth_bilar')
    c = conn.cursor()
    c.execute('SELECT * FROM bilar WHERE skraningarnumer = %s', (nr))
    bill = c.fetchone()

    conn.close()
    c.close()

    return template('updatecar', bill=bill)

@route('/db/update', method='POST')
def submit_update():
    skr_nr = request.forms.get('skr_nr')
    tegund = request.forms.tegund
    vrk_nr = request.forms.get('vrk_nr')
    skr_dags = request.forms.get('skr_dags')
    co2 = request.forms.get('co2')
    tyngd = request.forms.get('tyngd')
    sko_dags = request.forms.get('sko_dags')
    stada = request.forms.stada

    co2 = int(co2)
    tyngd = int(tyngd)

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2608993339', passwd='mypassword', db='2608993339_vefth_bilar')
    c = conn.cursor()

    c.execute("UPDATE bilar SET skraningarnumer='{}', tegund='{}', verksmidjunumer='{}', skraningardagur='{}', co2='{}', þyngd='{}', skodun='{}', stada='{}' where skraningarnumer = '{}'".format(skr_nr, tegund, vrk_nr, skr_dags, co2, tyngd, sko_dags, stada, skr_nr))
    conn.commit()

    conn.close()
    c.close()

    return redirect('/')
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
