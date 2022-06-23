from flask import Flask, render_template
from getpass import getuser

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/hello')
def hello():
	return render_template('hello.html')

@app.route('/hello/<name>/')
def helloName(name):
	return f'Hello, <code>{name}</code>!'

if __name__ == '__main__':
	app.run()
