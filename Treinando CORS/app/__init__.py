from flask import Flask
from flask_cors import CORS
from app.route import user_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(user_bp)

    return app