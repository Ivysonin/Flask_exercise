from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
# Carregando as variáveis de ambiente
load_dotenv('.env')


# Criando a aplicação Flask
app = Flask(__name__)


# Definindo onde vai ficar o banco de dados
            # Pegando a URI e colocando na configuração de app
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')


# Desabilidando o 'check' que faz a cada modificação(não é obrigatório)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Sempre pegar uma senha aleatória 
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


# Para o meu 'app' quero criar esse banco de dados
db = SQLAlchemy(app)

'''
Se precisar fazer alteração no banco,
não preciso alterar direto no banco de dados, 
por meio de comandos consigo alterar o arquivo e usar um comando que faz tudo automaticamente.
'''
migrate = Migrate(app, db)


from app.routes import homepage
from app.models import Contato