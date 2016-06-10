from flask import Flask, request, flash, render_template, session, redirect, url_for, abort

# Configuration


app = Flask(__name__)
app.config.update(
    DATABASE='',
    USERNAME='admin',
    PASSWORD='admin',
    SECRET_KEY='change_me'
    )

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
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add():
    if session.get('logged_in'):
        flash('New entry was successfully posted')
    else:
        abort(401)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
