from flask import Flask, render_template, request
from gpt2_text_generator import GPT2TextGenerator

app = Flask(__name__)

# Initialisiere Text-Generator mit deinen Wunschparametern
text_generator = GPT2TextGenerator(
    model_name="gpt2",   # oder z.B. "gpt2-medium"
    max_length=100,
    temperature=0.7,
    top_p=0.9
)

@app.route("/", methods=["GET", "POST"])
def home():
    generated_text = None

    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()
        if prompt:
            # Generiere Text anhand des Prompts
            results = text_generator.generate_text(prompt)
            generated_text = results[0]["generated_text"]

    return render_template("index.html", generated_text=generated_text)

if __name__ == "__main__":
    # Für produktives Deployment solltest du debug=False setzen.
    # Beispielsweise via Gunicorn oder Waitress ausführen.
    app.run(host="0.0.0.0", port=5000, debug=True)
