from app import app
from flask import render_template, url_for, redirect, request
from app.forms import ContatoForm, UserForm, LoginForm, PostForm, PostComentarioForm
from app.models import Contato, Post
from flask_login import login_user, current_user, logout_user

@app.route('/', methods=['GET', 'POST'])
def homepage():
    form = LoginForm()

    if form.validate_on_submit():
        # Fazendo o login do usuário
        user = form.login()
        login_user(user, remember=True)

    context = {
        'usuario':'Ivyson',
        'idade':16
    }
    return render_template('index.html', context=context, form=form)


@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro():
    form = UserForm()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template('cadastro.html', form=form)


# Deslogando o Usuário
@app.route('/sair/', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/post/novo/', methods=['GET', 'POST'])
def PostNovo():
    form = PostForm()
    if form.validate_on_submit():
        form.save(current_user.id)
        return redirect(url_for('homepage'))

    return render_template('post_novo.html', form=form)


@app.route('/post/lista/')
def PostLista():
    posts = Post.query.all()

    return render_template('post_lista.html', posts=posts)


@app.route('/post/<int:id>', methods=['GET', 'POST'])
def PostDetail(id):
    post = Post.query.get(id)
    form = PostComentarioForm()

    if form.validate_on_submit():
        form.save(current_user.id, id)
        return redirect(url_for('PostDetail', id=id))

    return render_template('post.html', post=post, form=form)


@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    
    return render_template('contato.html', context=context, form=form)


@app.route('/contato/lista/')
def contatoLista():
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')

    dados = Contato.query.order_by('nome')
    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)

    context = {'dados':dados.all()}
    return render_template('contato_lista.html', context=context)


# Rota dinâmica
@app.route('/contato/<int:id>/')
def contatoDetail(id):
    obj = Contato.query.get(id)

    return render_template('contato_detail.html', obj=obj)