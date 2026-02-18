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
MODELS = [
    {
        'name': 'dolphin-mistral',
        'description': 'Dolphin Mistral 7B',
        'details': 'Balanced quality and speed'
    },
    {
        'name': 'dolphin-llama3',
        'description': 'Dolphin Llama3 8B',
        'details': 'High quality'
    },
    {
        'name': 'wizardlm-uncensored',
        'description': 'WizardLM Uncensored 7B',
        'details': 'Instruction-tuned'
    },
    {
        'name': 'nous-hermes-uncensored',
        'description': 'Nous Hermes Uncensored',
        'details': 'Creative'
    }
]

# UI formatting constant
SEPARATOR = "=" * 60
