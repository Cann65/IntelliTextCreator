import pytest
from app import create_app
from unittest.mock import MagicMock

@pytest.fixture
def client():
    app = create_app()
    
    # Mock den TEXT_GENERATOR
    text_generator_mock = MagicMock()
    text_generator_mock.generate_text.return_value = "Mocked generated text"
    app.config["TEXT_GENERATOR"] = text_generator_mock
    
    # Test-Client erstellen
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Generierter Text" in response.data
