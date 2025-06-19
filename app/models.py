from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin


# Retorna o usuário a partir do ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# 'UserMixin' usado para informar que essa tabela é de usuário para controle de login
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    sobrenome = db.Column(db.String, nullable=False)
    email =  db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    posts = db.relationship('Post', backref='user', lazy=True) # Não é uma coluna e sim uma relação
    post_comentarios = db.relationship('PostComentarios', backref='user', lazy=True) # Não é uma coluna e sim uma relação


class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow()) # utcnow: Pegando horário padrão universal
    nome = db.Column(db.String, nullable=False)
    email =  db.Column(db.String, nullable=False)
    assunto = db.Column(db.String, nullable=True)
    mensagem = db.Column(db.String, nullable=True)
    respondido = db.Column(db.Integer, default=0)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow()) # utcnow: Pegando horário padrão universal
    mensagem = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comentarios = db.relationship('PostComentarios', backref='post', lazy=True) # Não é uma coluna e sim uma relação

    def msg_resumo(self):
        return f"{self.mensagem[:10]}..."


class PostComentarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow())
    comentario = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)