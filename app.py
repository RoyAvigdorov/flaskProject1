from flask import Flask, redirect, render_template,session,request,url_for
from interact_with_DB import *


app = Flask(__name__)

@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_func():
    return render_template('Cv.html')


@app.route('/movies')
def tv():
    return render_template('movies.html')


@app.route('/assignment8')
def assigment8():
    return render_template('Assignment8.html',
                           user={'firstname': "Roy", 'lastname': "Avigdorov"},
                           hobbies=['movies', 'Hockey', 'Tennis'])


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    username = ''
    users = [{'id': 1, 'email': "roy.a@gmail.com", 'firstname': "roy", 'lastname': "avigdorov"},
        {'id': 2, 'email': "noam.Sul@gmail.com", 'firstname': "noam", 'lastname': "shulanski"},
        {'id': 3, 'email': "yoni.amid@gmail.com", 'firstname': "yoni", 'lastname': "amid"},
        {'id': 4, 'email': "tal.sorek@gmail.com", 'firstname': "tal", 'lastname': "sorek"},
        {'id': 5, 'email': "tom.kara@gmail.com", 'firstname': "tom", 'lastname': "kara"}]
    firstname = ''
    logged_in = True

    if request.method == 'GET':
        if 'firstname' in request.args:
            firstname = request.args['firstname']

    if request.method == 'POST':
        username = request.form['username']
        session['logged_in'] = True
        session['username'] = username
    return render_template('Assignment9.html',
                           request_method=request.method,
                           name=firstname,
                           users=users,
                           username=username)


@app.route('/log_out')
def log_out():
    session.pop('username')
    session['logged_in'] = False
    session['username'] = ''
    return redirect('/assignment9')

## assignment10
from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)



if __name__ == '__main__':
    app.run(debug=True)


