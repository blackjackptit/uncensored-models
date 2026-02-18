#!/usr/bin/env python3
"""
Ollama Utilities Module
=======================

Shared utility functions for interacting with Ollama.
This module provides a consistent interface for Ollama operations
across all scripts in the project.

Functions:
    verify_ollama() -> tuple[bool, str | None]
    check_ollama_running() -> bool
    list_installed_models() -> str
    download_model(name: str) -> bool
    download_all_models(interactive: bool) -> bool
    setup_environment() -> bool
    print_env_setup_instructions() -> None

Usage:
    from ollama_utils import verify_ollama, download_all_models

    is_installed, version = verify_ollama()
    if is_installed:
        download_all_models(interactive=True)
"""

import os
import subprocess
from config import MODEL_DIR, MODELS, SEPARATOR


def verify_ollama():
    """
    Check if Ollama is installed and get version information.

    Returns:
        tuple: (is_installed: bool, version: str | None)
            - is_installed: True if Ollama is found and working
            - version: Version string if available, None otherwise

    Example:
        >>> is_installed, version = verify_ollama()
        >>> if is_installed:
        ...     print(f"Ollama version: {version}")
    """
    try:
        result = subprocess.run(
            ['ollama', '--version'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        if result.returncode == 0:
            return True, result.stdout.strip()
        return False, None
    except FileNotFoundError:
        return False, None


def check_ollama_running():
    """
    Check if the Ollama service is running and responsive.

    Returns:
        bool: True if Ollama responds to commands, False otherwise

    Note:
        This performs a lightweight check using 'ollama list' command.
        It's faster than verify_ollama() but doesn't return version info.
    """
    try:
        result = subprocess.run(
            ['ollama', 'list'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def list_installed_models():
    """
    Get a formatted list of all models currently installed.

    Returns:
        str: Formatted output from 'ollama list' command, or empty string on failure

    Example output:
        NAME                    ID              SIZE    MODIFIED
        dolphin-mistral:latest  abc123def456    4.1 GB  2 days ago
    """
    try:
        result = subprocess.run(
            ['ollama', 'list'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        return result.stdout if result.returncode == 0 else ""
    except Exception:
        return ""


def download_model(model_name):
    """
    Download a single model from the Ollama registry.

    Args:
        model_name (str): Name of the model to download (e.g., 'dolphin-mistral')

    Returns:
        bool: True if download succeeded, False otherwise

    Note:
        Downloads to the directory specified by MODEL_DIR via OLLAMA_MODELS env var.
    """
    try:
        result = subprocess.run(
            ['ollama', 'pull', model_name],
            env={**os.environ, 'OLLAMA_MODELS': str(MODEL_DIR)}
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Error downloading {model_name}: {e}")
        return False


def download_all_models(interactive=True):
    """
    Download all models configured in the MODELS list.

    Args:
        interactive (bool): If True, prompts user for confirmation before downloading.
                          If False, proceeds automatically.

    Returns:
        bool: True if at least one model downloaded successfully, False otherwise

    Note:
        Displays progress for each model and provides a summary at the end.
        Models are downloaded sequentially to avoid overwhelming the system.
    """
    print(f"\n{SEPARATOR}")
    print("DOWNLOADING MODELS")
    print(SEPARATOR)
    print("\nThe following models will be downloaded:")
    for model in MODELS:
        print(f"  • {model['description']} - {model['details']}")
    print(f"\nDownload location: {MODEL_DIR}")
    print(SEPARATOR)

    if interactive:
        proceed = input("\nProceed with download? (y/n): ").strip().lower()
        if proceed != 'y':
            print("Download cancelled.")
            return False

    success_count = 0
    for model in MODELS:
        print(f"\n{SEPARATOR}")
        print(f"Downloading: {model['name']}")
        print(SEPARATOR)

        if download_model(model['name']):
            print(f"✓ Successfully downloaded {model['name']}")
            success_count += 1
        else:
            print(f"✗ Failed to download {model['name']}")

    print(f"\n{SEPARATOR}")
    print(f"Download complete: {success_count}/{len(MODELS)} models")
    print(SEPARATOR)

    return success_count > 0


def setup_environment():
    """
    Set up the environment for Ollama operations.

    Actions:
        1. Creates the MODEL_DIR directory if it doesn't exist
        2. Sets OLLAMA_MODELS environment variable for current session

    Returns:
        bool: Always returns True

    Note:
        This only affects the current Python session. For persistent setup,
        use print_env_setup_instructions() to get system-level setup commands.
    """
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    os.environ['OLLAMA_MODELS'] = str(MODEL_DIR)
    return True


def print_env_setup_instructions():
    """
    Display instructions for setting OLLAMA_MODELS permanently on Windows.

    Prints formatted instructions for:
        - PowerShell (Administrator)
        - Command Prompt (Administrator)
        - Restarting Ollama service

    Note:
        After following these instructions, the Ollama service will
        automatically use the custom model directory for all future operations.
    """
    print(f"\n{SEPARATOR}")
    print("IMPORTANT: Setting OLLAMA_MODELS environment variable")
    print(SEPARATOR)
    print("\nFor persistent setup, set the environment variable:")
    print(f"\nWindows (PowerShell as Administrator):")
    print(f'[System.Environment]::SetEnvironmentVariable("OLLAMA_MODELS", "{MODEL_DIR}", "Machine")')
    print(f"\nWindows (Command Prompt as Administrator):")
    print(f'setx OLLAMA_MODELS "{MODEL_DIR}" /M')
    print("\nAfter setting, restart the Ollama service:")
    print("1. Open Task Manager")
    print("2. End the 'Ollama' process")
    print("3. Start Ollama again")
    print(SEPARATOR)
