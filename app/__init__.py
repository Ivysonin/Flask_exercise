from flask import Flask

# Criando a aplicação Flask
app = Flask(__name__)

from app.routes import homepage