import os
import logging

# Basis-Konfiguration
class Config:
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt2")
    MAX_LENGTH = int(os.getenv("MAX_LENGTH", 100))
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
    TOP_P = float(os.getenv("TOP_P", 0.9))

    # Logging-Konfiguration
    LOG_LEVEL = logging.INFO  # oder DEBUG, WARNING, ERROR, CRITICAL
