from flask import Flask
from app.routes.user import usuario_bp
from app.routes.produtos import produtos_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(usuario_bp)
    app.register_blueprint(produtos_bp)

    return app