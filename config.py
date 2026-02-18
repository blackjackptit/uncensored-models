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
MODELS = [
    # PREMIUM UNCENSORED MODELS (Best Quality - Higher RAM required)
    {
        'name': 'dolphin-llama3:70b',
        'description': 'Dolphin Llama3 70B Uncensored',
        'details': 'BEST OVERALL - Highest quality, excellent reasoning (~40GB RAM)'
    },
    {
        'name': 'dolphin-mixtral:8x7b',
        'description': 'Dolphin Mixtral 8x7B Uncensored',
        'details': 'EXCELLENT - Top reasoning & instruction following (~26GB RAM)'
    },
    {
        'name': 'dolphin-llama3:34b',
        'description': 'Dolphin Llama3 34B Uncensored',
        'details': 'HIGH QUALITY - Great balance of quality and speed (~20GB RAM)'
    },

    # RECOMMENDED UNCENSORED MODELS (Best Balance - Fast & Capable)
    {
        'name': 'dolphin-llama3:8b',
        'description': 'Dolphin Llama3 8B Uncensored',
        'details': 'Best 8B uncensored model - High quality, fast responses (~8GB RAM)'
    },
    {
        'name': 'dolphin-mistral:7b',
        'description': 'Dolphin Mistral 7B Uncensored',
        'details': 'Fast & reliable uncensored model, excellent general purpose (~8GB RAM)'
    },
    {
        'name': 'dolphin2.2-mistral:7b',
        'description': 'Dolphin 2.2 Mistral 7B Uncensored',
        'details': 'Refined uncensored version, excellent instruction following (~8GB RAM)'
    },

    # CLASSIC UNCENSORED MODELS
    {
        'name': 'wizardlm-uncensored:13b',
        'description': 'WizardLM Uncensored 13B',
        'details': 'Classic uncensored model, great for instructions and tasks (~13GB RAM)'
    },
    {
        'name': 'nous-hermes-llama2-uncensored:13b',
        'description': 'Nous Hermes Llama2 Uncensored 13B',
        'details': 'Reliable uncensored model, versatile and capable (~13GB RAM)'
    },
    {
        'name': 'orca2-uncensored:7b',
        'description': 'Orca 2 Uncensored 7B',
        'details': 'Fast uncensored model with good reasoning abilities (~8GB RAM)'
    }
]

# UI formatting constant
SEPARATOR = "=" * 60
