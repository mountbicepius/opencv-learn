from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
	return 'Index Page'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/syaci')
@app.route('/syaci/<params>')
def syaci_eval(params=None)
	return render_template('syaci.html', params=params)