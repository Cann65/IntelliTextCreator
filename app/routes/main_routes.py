from flask import Blueprint, render_template, request, current_app
import logging

main_bp = Blueprint("main_bp", __name__, template_folder="../templates")
logger = logging.getLogger(__name__)

@main_bp.route("/", methods=["GET", "POST"])
def home():
    generated_text = None

    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()
        if prompt:
            # Greife auf die GPT2TextGenerator-Instanz aus der App-Konfiguration zu
            text_generator = current_app.config.get("TEXT_GENERATOR")
            if text_generator:
                logger.info("Prompt empfangen. Generiere Text...")
                generated_text = text_generator.generate_text(prompt)
            else:
                logger.error("TEXT_GENERATOR ist nicht in current_app.config konfiguriert!")

    return render_template("index.html", generated_text=generated_text)
