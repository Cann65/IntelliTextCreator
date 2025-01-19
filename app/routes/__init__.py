import logging
from flask import Flask
from config import Config

def create_app():
    # Flask-App erstellen
    app = Flask(__name__)
    
    # Konfiguration einlesen
    app.config.from_object(Config)
    
    # Logging konfigurieren
    logging.basicConfig(
        level=app.config["LOG_LEVEL"],
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("logs/app.log", mode="a", encoding="utf-8")
        ]
    )
    
    # Blueprints importieren
    from app.routes.main_routes import main_bp
    from app.routes.api_routes import api_bp
    
    # Blueprints registrieren
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    
    return app
