from app import app
from flask import render_template, url_for, redirect
from app.forms import ContatoForm

@app.route('/')
def homepage():
    context = {
        'usuario':'Ivyson',
        'idade':16
    }
    return render_template('index.html', context=context)


@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    
    return render_template('contato.html', context=context, form=form)