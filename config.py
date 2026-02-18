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

# UNCENSORED MODELS ONLY - No content restrictions
# To add a new model, append to this list:
# - 'name': The model identifier used by Ollama (e.g., from 'ollama pull <name>')
# - 'description': Short description shown in model selection
# - 'details': Additional details about capabilities or use cases
#
# All models below are FULLY UNCENSORED with no content filtering
# Your system has 48GB RAM - can run up to 70B models
# VERIFIED: All model names tested and confirmed to exist on Ollama registry
MODELS = [
    # PREMIUM UNCENSORED MODELS (Best Quality - Higher RAM required)
    {
        'name': 'dolphin-mixtral:8x7b',
        'description': 'Dolphin Mixtral 8x7B Uncensored',
        'details': 'BEST AVAILABLE - Top reasoning & instruction following (~26GB RAM)'
    },

    # RECOMMENDED UNCENSORED MODELS (Best Balance - Fast & Capable)
    {
        'name': 'dolphin-llama3:latest',
        'description': 'Dolphin Llama3 8B Uncensored',
        'details': 'Best 8B uncensored model - High quality, fast responses (~8GB RAM)'
    },
    {
        'name': 'dolphin-mistral:latest',
        'description': 'Dolphin Mistral 7B Uncensored',
        'details': 'Fast & reliable uncensored model, excellent general purpose (~8GB RAM)'
    },
    {
        'name': 'wizardlm-uncensored:13b',
        'description': 'WizardLM Uncensored 13B',
        'details': 'Classic uncensored model, great for instructions and tasks (~13GB RAM)'
    }
]

# UI formatting constant
SEPARATOR = "=" * 60
