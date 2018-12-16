from flask import (Flask, make_response, redirect, render_template, request,
                   url_for)

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class my_form(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    # submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'pku_phy'


@app.route('/')
def index():
    response = make_response('<h1>Index page</h1>')
    return response


@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = my_form()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def profile(username):
    return 'User: %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post: '+str(post_id)


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath: '+str(subpath)


@app.route('/login')
def login():
    return 'login...'


'''
with app.test_request_context():
    print(url_for('show_post',post_id=123,_external=True))
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
'''
if __name__ == '__main__':
    app.run(debug=True)
