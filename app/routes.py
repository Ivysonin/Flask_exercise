from app import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    context = {
        'usuario':'Ivyson',
        'idade':16
    }
    return render_template('index.html', context=context)

@app.route('/novapágina')
def novapag():
    return 'Segunda página web'