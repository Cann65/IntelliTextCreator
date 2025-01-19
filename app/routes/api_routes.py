from flask import Blueprint, request, jsonify, current_app
import logging

api_bp = Blueprint("api_bp", __name__)
logger = logging.getLogger(__name__)

@api_bp.route("/generate_text", methods=["POST"])
def api_generate_text():
    data = request.json or {}
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"error": "Missing 'prompt' in JSON body"}), 400

    text_generator = current_app.config.get("TEXT_GENERATOR")
    if not text_generator:
        logger.error("No text generator found in current_app.config!")
        return jsonify({"error": "Internal configuration error"}), 500

    generated_text = text_generator.generate_text(prompt)
    return jsonify({"generated_text": generated_text})
