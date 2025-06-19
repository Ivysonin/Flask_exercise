from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import data_required, Email, EqualTo, ValidationError
from app import db, bcrypt
from app.models import Contato, User, Post, PostComentarios


class UserForm(FlaskForm):
    nome = StringField('Nome', validators=[data_required()])
    sobrenome = StringField('Sobrenome', validators=[data_required()])
    email = StringField('E-Mail', validators=[data_required(), Email()])
    senha = PasswordField('Senha', validators=[data_required()])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[data_required(), EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')

    def validate_email(self, email):
        # Estou acessando o db e procurando se tem algum 'email' igual, se tiver retorna um erro.
        if User.query.filter(User.email == email.data).first():
            return ValidationError('Usuário Já Cadastrado com esse E-mail!!!')

    def save(self):
        # Criptografando a senha
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
        user = User(
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha = senha
        )
        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[data_required(), Email()])
    senha = PasswordField('Senha', validators=[data_required()])
    btnSubmit = SubmitField('Login')

    def login(self):
        # Recuperando o usuário do e-mail
        user = User.query.filter_by(email=self.email.data).first()

        # Verifica se está vindo um usuário
        if user: 
            # Verificando se a senha é valida
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                return user
            else:
                raise Exception('Senha incorreta!!!')
        else:
            raise Exception('Usuário não encontrado!!!')


class ContatoForm(FlaskForm):
    # Sempre passa primeiro o nome.
    nome = StringField('Nome', validators=[data_required()])
    email =  StringField('E-Mail', validators=[data_required(), Email()])
    assunto = StringField('Assunto', validators=[data_required()])
    mensagem = StringField('Mensagem', validators=[data_required()])
    btnSubmit = SubmitField('Enviar')
    
    def save(self):
        contato = Contato(
            # .data para acessar o valor em string, e não o objeto de StringField()
            nome = self.nome.data, 
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
        )

        db.session.add(contato)
        db.session.commit()


class PostForm(FlaskForm):
    mensagem = StringField('Mensagem', validators=[data_required()])
    btnSubmit = SubmitField('Enviar')

    def save(self, user_id):
        post = Post(
            mensagem=self.mensagem.data,
            user_id=user_id
        )

        db.session.add(post)
        db.session.commit()


class PostComentarioForm(FlaskForm):
    comentario = StringField('Comentário', validators=[data_required()])
    btnSubmit = SubmitField('Enviar')

    def save(self, user_id, post_id):
        comentario = PostComentarios(
            comentario=self.comentario.data,
            user_id=user_id,
            post_id=post_id
        )

        db.session.add(comentario)
        db.session.commit()