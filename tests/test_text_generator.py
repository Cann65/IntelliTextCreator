import pytest
from models.text_generator import GPT2TextGenerator

def test_generate_text():
    generator = GPT2TextGenerator(
        model_name="gpt2",
        max_length=10,
        temperature=0.7,
        top_p=0.9
    )
    output = generator.generate_text("Hallo Welt")
    assert isinstance(output, str)
    assert len(output) > 0
