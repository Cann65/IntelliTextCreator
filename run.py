from app import create_app
from models.text_generator import GPT2TextGenerator

def main():
    # Erstelle die Flask-App
    app = create_app()

    # Initialisiere den GPT-2-Textgenerator
    text_generator = GPT2TextGenerator(
        model_name=app.config["MODEL_NAME"],
        max_length=app.config["MAX_LENGTH"],
        temperature=app.config["TEMPERATURE"],
        top_p=app.config["TOP_P"]
    )

    # Registriere den Textgenerator in der App-Konfiguration
    app.config["TEXT_GENERATOR"] = text_generator

    # Starte die App
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == "__main__":
    main()
