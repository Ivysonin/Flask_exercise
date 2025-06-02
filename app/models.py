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


class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow()) # utcnow: Pegando horário padrão universal
    nome = db.Column(db.String, nullable=False)
    email =  db.Column(db.String, nullable=False)
    assunto = db.Column(db.String, nullable=True)
    mensagem = db.Column(db.String, nullable=True)
    respondido = db.Column(db.Integer, default=0)