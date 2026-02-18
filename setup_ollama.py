#!/usr/bin/env python3
"""
Setup Script for Ollama Uncensored Models
==========================================

This script performs initial setup for the uncensored models project:
1. Verifies Ollama is installed
2. Creates and configures the model directory
3. Downloads all configured models
4. Provides instructions for permanent environment setup

Usage:
    python setup_ollama.py

Requirements:
    - Ollama must be installed from https://ollama.ai
    - Administrator privileges recommended for environment variable setup
    - ~20 GB free disk space for all models

The script will:
    - Check Ollama installation and version
    - Create D:\\llm-models directory
    - Set OLLAMA_MODELS for current session
    - Prompt to download all models
    - Display persistent setup instructions
"""

import sys
from config import MODEL_DIR, SEPARATOR
from ollama_utils import (
    verify_ollama,
    setup_environment,
    print_env_setup_instructions,
    download_all_models
)


def main():
    """
    Main setup routine.

    Workflow:
        1. Verify Ollama installation
        2. Setup environment and model directory
        3. Display persistent setup instructions
        4. Download models (with user confirmation)
        5. Display completion message
    """
    print(f"\n{SEPARATOR}")
    print("UNCENSORED MODELS SETUP")
    print(SEPARATOR)

    # Verify Ollama is installed
    is_installed, version = verify_ollama()
    if not is_installed:
        print("✗ Ollama is not installed")
        print("\nInstallation steps:")
        print("1. Visit https://ollama.ai")
        print("2. Download Ollama for Windows")
        print("3. Run the installer")
        print("4. Run this setup script again")
        sys.exit(1)

    print(f"✓ Ollama version: {version}")

    # Setup directory and environment
    setup_environment()
    print(f"\n✓ Model directory created: {MODEL_DIR}")
    print(f"✓ OLLAMA_MODELS set to: {MODEL_DIR}")

    # Show environment setup instructions
    print_env_setup_instructions()

    # Download models
    print("\n")
    download_all_models(interactive=True)

    print(f"\n{SEPARATOR}")
    print("SETUP COMPLETE")
    print(SEPARATOR)
    print("\nTo start chatting, run:")
    print("  python chat.py")
    print("\nRemember to set the OLLAMA_MODELS environment variable")
    print("permanently using the commands shown above!")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
