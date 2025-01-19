from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

class GPT2TextGenerator:
    def __init__(self, model_name, max_length, temperature, top_p):
        """
        Initialisiert die GPT-2 Pipeline und speichert die Konfigurationsparameter.
        """
        logger.info("Initialisiere GPT-2 Pipeline mit dem Modell: %s", model_name)
        self.generator = pipeline("text-generation", model=model_name)
        self.max_length = max_length
        self.temperature = temperature
        self.top_p = top_p
        logger.info("GPT-2 Pipeline erfolgreich geladen.")

    def generate_text(self, prompt, num_return_sequences=1):
        """
        Generiert Text basierend auf einem gegebenen Prompt.
        """
        logger.info("Prompt empfangen: %s", prompt)

        # Generiere Text
        results = self.generator(
            prompt,  # Der Prompt wird direkt als String übergeben
            max_length=self.max_length,
            temperature=self.temperature,
            top_p=self.top_p,
            num_return_sequences=num_return_sequences
        )

        # Gib den generierten Text zurück
        generated_text = results[0]["generated_text"]
        logger.info("Generierter Text: %s", generated_text)
        return generated_text
