import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
import pywapi
import string
import time
import variables

DATABASE = 'entries.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('ATMOSITY_SETTINGS', silent=True)

time = time.strftime("%a, %m/%d/%Y - %r", time.localtime())

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select time_stamp, temperature, humidity, pressure from entries order by id desc')
    entries = [dict(time_stamp=row[0], temperature=row[1], humidity=row[2], pressure=row[3]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries, unit=variables.unit,
                             convert_temp=convert_temp, convert_pressure=convert_pressure)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    weather = pywapi.get_weather_from_weather_com(str(variables.zip), 'metric')
    g.db.execute('insert into entries (time_stamp, temperature, humidity, pressure) values (?, ?, ?, ?)',
                 [str(time),
                  str(weather['current_conditions']['temperature']),
                  str(weather['current_conditions']['humidity']),
                  str(weather['current_conditions']['barometer']['reading'])])

    g.db.commit()
    flash('New data was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/flush')
def flush():
    g.db.execute('delete from entries')
    g.db.commit()

    return redirect(url_for('show_entries'))

@app.route('/change_unit')
def change_unit():
    if variables.unit == 'metric':
        variables.unit = 'imperial'
    else:
        variables.unit = 'metric'
    flash('Units have changed to ' + variables.unit)
    return redirect(url_for('show_entries'))

def convert_temp(temp):
    return (float(temp) * 1.8 + 32)

def convert_pressure(pressure):
    return (float(pressure) * 6894.76)

if __name__ == '__main__':
    app.run()
