from app import db
from datetime import datetime

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow()) # utcnow: Pegando horário padrão universal
    nome = db.Column(db.String, nullable=False)
    email =  db.Column(db.String, nullable=False)
    assunto = db.Column(db.String, nullable=True)
    mensagem = db.Column(db.String, nullable=True)
    respondido = db.Column(db.Integer, default=0)