from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def id(username):
    return 'Hello, %s !' % username

@app.route('/user/real/<name>')
def profile(name):
    return render_template('profile.html', name=name)

app.run()