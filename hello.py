from flask import Flask, url_for,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)


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
