from app import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/novapágina')
def novapag():
    return 'Segunda página web'