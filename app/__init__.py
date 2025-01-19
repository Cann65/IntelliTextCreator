from flask import Flask
from config import Config

def create_app():
    # Flask-App erstellen
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registriere die Blueprints
    from app.routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app
