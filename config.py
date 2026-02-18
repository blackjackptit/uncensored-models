#!/usr/bin/env python3
"""
Configuration Module
====================

Centralized configuration for the uncensored models project.
This is the single source of truth for all configuration values.

Usage:
    from config import MODEL_DIR, MODELS, SEPARATOR

Attributes:
    MODEL_DIR (Path): Directory where Ollama models are stored
    MODELS (list): List of available model configurations
    SEPARATOR (str): Formatting separator for CLI output
"""

from pathlib import Path

# Model storage directory
# This path will be set as the OLLAMA_MODELS environment variable
MODEL_DIR = Path("D:/llm-models")

# Available uncensored models
# To add a new model, append to this list:
# - 'name': The model identifier used by Ollama (e.g., from 'ollama pull <name>')
# - 'description': Short description shown in model selection
# - 'details': Additional details about capabilities or use cases
#
# Models organized by size/capability (your system has 48GB RAM - can run up to 70B models)
MODELS = [
    # PREMIUM MODELS (Best Quality - Higher RAM required)
    {
        'name': 'dolphin-llama3:70b',
        'description': 'Dolphin Llama3 70B',
        'details': 'BEST OVERALL - Highest quality, excellent reasoning (~40GB RAM)'
    },
    {
        'name': 'dolphin-mixtral:8x7b',
        'description': 'Dolphin Mixtral 8x7B',
        'details': 'EXCELLENT - Top reasoning & instruction following (~26GB RAM)'
    },
    {
        'name': 'dolphin-llama3:34b',
        'description': 'Dolphin Llama3 34B',
        'details': 'HIGH QUALITY - Great balance of quality and speed (~20GB RAM)'
    },

    # RECOMMENDED MODELS (Best Balance - Fast & Capable)
    {
        'name': 'dolphin-llama3:8b',
        'description': 'Dolphin Llama3 8B',
        'details': 'Best 8B model - High quality, fast responses (~8GB RAM)'
    },
    {
        'name': 'wizardlm2:7b',
        'description': 'WizardLM2 7B',
        'details': 'Great for coding & complex instructions (~8GB RAM)'
    },
    {
        'name': 'dolphin-mistral:7b',
        'description': 'Dolphin Mistral 7B',
        'details': 'Fast & reliable, good general purpose (~8GB RAM)'
    },

    # SPECIALIZED MODELS
    {
        'name': 'nous-hermes2-mixtral:8x7b',
        'description': 'Nous Hermes 2 Mixtral 8x7B',
        'details': 'Creative writing & roleplay focused (~26GB RAM)'
    },
    {
        'name': 'nous-hermes2:34b',
        'description': 'Nous Hermes 2 34B',
        'details': 'Creative conversations, versatile (~20GB RAM)'
    },
    {
        'name': 'openhermes:7b',
        'description': 'OpenHermes 7B',
        'details': 'Precise instruction following, good for tasks (~8GB RAM)'
    }
]

# UI formatting constant
SEPARATOR = "=" * 60
