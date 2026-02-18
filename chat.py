#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Chat Interface for Uncensored Models
================================================

A command-line interface for chatting with uncensored language models
through Ollama. Supports multiple models, conversation history, and
runtime model switching.

Usage:
    python chat.py

Features:
    - Interactive model selection
    - Persistent conversation history per session
    - Runtime commands (/clear, /models, exit, quit)
    - Automatic environment setup

Commands:
    exit, quit  - Exit the chat application
    /clear      - Clear conversation history
    /models     - Switch to a different model

Requirements:
    - Ollama must be installed and running
    - At least one model must be downloaded
"""

import sys
import subprocess

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
from config import MODELS, SEPARATOR
from ollama_utils import (
    check_ollama_running,
    list_installed_models,
    setup_environment
)


def select_model():
    """
    Display available models and let user select one.

    Returns:
        str: Name of the selected model

    Note:
        If user enters an invalid choice, defaults to the first model
        in the MODELS list (typically dolphin-mistral).
    """
    print(f"\n{SEPARATOR}")
    print("AVAILABLE UNCENSORED MODELS")
    print(SEPARATOR)

    # Create numbered dict for selection
    model_dict = {str(i+1): model for i, model in enumerate(MODELS)}

    for key, model in model_dict.items():
        print(f"{key}. {model['description']} - {model['details']}")
    print(SEPARATOR)

    choice = input(f"\nSelect model (1-{len(MODELS)}): ").strip()
    if choice in model_dict:
        return model_dict[choice]['name']
    else:
        print("Invalid choice, using default (Dolphin Mistral)")
        return MODELS[0]['name']


def chat(model_name):
    """
    Start an interactive chat session with the specified model.

    Args:
        model_name (str): Name of the Ollama model to use

    Returns:
        bool: True if user wants to switch models, False if exiting

    Features:
        - Maintains conversation history throughout the session
        - Supports special commands (/clear, /models)
        - Handles keyboard interrupts gracefully
        - Formats conversation context for the model

    Note:
        The conversation history is maintained by concatenating all
        previous messages into a single prompt for context continuity.
    """
    print(f"\n{SEPARATOR}")
    print(f"Starting chat with {model_name}")
    print(SEPARATOR)
    print("Type 'exit', 'quit', or press Ctrl+C to end the conversation")
    print("Type '/clear' to clear conversation history")
    print("Type '/models' to switch models")
    print(f"{SEPARATOR}\n")

    conversation = []

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit']:
                print("\nGoodbye!")
                break

            if user_input == '/clear':
                conversation = []
                print("\n[Conversation history cleared]\n")
                continue

            if user_input == '/models':
                return True  # Signal to restart with model selection

            # Add user message to conversation
            conversation.append({
                "role": "user",
                "content": user_input
            })

            # Build the prompt
            prompt = ""
            for msg in conversation:
                if msg["role"] == "user":
                    prompt += f"User: {msg['content']}\n"
                else:
                    prompt += f"Assistant: {msg['content']}\n"
            prompt += "Assistant: "

            # Call ollama
            result = subprocess.run(
                ['ollama', 'run', model_name, prompt],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                print(f"\nError: {result.stderr}")
                continue

            response = result.stdout.strip()

            # Add assistant response to conversation
            conversation.append({
                "role": "assistant",
                "content": response
            })

            print(f"\n{model_name}: {response}\n")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            continue

    return False




def main():
    """
    Main entry point for the chat application.

    Workflow:
        1. Setup environment variables
        2. Verify Ollama is running
        3. Display installed models
        4. Enter chat loop with model selection
        5. Allow switching models without restarting
    """
    print(f"\n{SEPARATOR}")
    print("UNCENSORED LLM CHAT")
    print(SEPARATOR)

    # Setup environment
    setup_environment()

    # Check if Ollama is installed
    if not check_ollama_running():
        print("\n⚠️  Ollama is not installed or not running!")
        print("\nTo install Ollama:")
        print("1. Download from: https://ollama.ai")
        print("2. Run the installer")
        print("3. Restart this script")
        print("\nAfter installation, run: python setup_ollama.py")
        sys.exit(1)

    print("\n✓ Ollama is installed and running")

    # Show installed models
    print("\nInstalled models:")
    print(list_installed_models())

    # Start chat loop
    while True:
        model_name = select_model()
        should_continue = chat(model_name)
        if not should_continue:
            break


if __name__ == "__main__":
    main()
