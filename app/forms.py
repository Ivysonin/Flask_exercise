from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required, Email
from app import db
from app.models import Contato

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