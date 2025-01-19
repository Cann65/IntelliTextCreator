from transformers import pipeline

class GPT2TextGenerator:
    def __init__(self,
                 model_name="gpt2",
                 max_length=100,
                 temperature=0.7,
                 top_p=0.9):
        """
        Initialisiert die GPT-2 Pipeline mit den angegebenen Parametern.
        """
        print("Initializing GPT-2 pipeline with model_name:", model_name)
        self.generator = pipeline("text-generation", model=model_name)

  
        self.max_length = max_length
        self.temperature = temperature
        self.top_p = top_p

    def generate_text(self, prompt, num_return_sequences=1):
        """
        Erzeugt mithilfe der GPT-2-Pipeline Text auf Grundlage des Prompts.
        """
        results = self.generator(
            prompt,
            max_length=self.max_length,
            temperature=self.temperature,
            top_p=self.top_p,
            num_return_sequences=num_return_sequences
        )
        return results
