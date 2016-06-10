from flask import Flask, request, flash, render_template, session, redirect, url_for, abort, g
import sqlite3

# Configuration


app = Flask(__name__)
app.config.update(
    DATABASE='flaskr.db',
    DATABASE_PATH='./flaskr.db',
    USERNAME='admin',
    PASSWORD='admin',
    SECRET_KEY='change_me'
    )

#connect to database
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE_PATH'])
    rv.row_factory = sqlite3.Row
    return rv

#create the database
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
            db.commit()

#open the database connection
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

#close the database connection
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/hello')
def hello():
    return 'Hello World!'


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
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))


@app.route('/index')
def index():
    db = get_db()
    cur = db.execute('SELECT title, text FROM entries ORDER BY id DESC ')
    entries = cur.fetchall()
    return render_template('index.html', entries=entries)


@app.route('/add', methods=['POST'])
def add():
    if session.get('logged_in'):
        db = get_db()
        cur = db.execute('INSERT INTO entries (title, text) VALUES (?, ?)',
                         [request.form['title'], request.form['text']])
        db.commit()
        flash('New entry was successfully posted')
    else:
        abort(401)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
