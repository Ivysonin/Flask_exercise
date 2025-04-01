from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Criando a aplicação Flask
app = Flask(__name__)


# Definindo onde vai ficar o banco de dados
            # Pegando a URI e colocando na configuração de app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
                                        # Definindo qual que é o caminho(vai criar um arquivo quando rodar o comando para criar o banco de dados)

# Desabilidando o 'check' que faz a cada modificação(não é obrigatório)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

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