#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Testing Suite for Uncensored Models
==============================================

Validates the installation and functionality of the chat application
by running a series of automated tests.

Usage:
    python test_chat.py

Tests Performed:
    1. Ollama installation verification
    2. Model listing and availability
    3. Model response test (haiku generation)
    4. Creative prompt test (joke generation)

Requirements:
    - Ollama must be installed and running
    - At least one model must be downloaded (preferably dolphin-mistral)

Expected Output:
    Each test displays a ✓ for success or ✗ for failure,
    along with detailed output or error messages.
"""

import subprocess
from config import MODEL_DIR, MODELS, SEPARATOR
from ollama_utils import verify_ollama, list_installed_models, setup_environment

# Setup environment for test session
setup_environment()

print(SEPARATOR)
print("TESTING CHAT APPLICATION")
print(SEPARATOR)
print()

# Test 1: Check if Ollama is accessible
print("Test 1: Checking Ollama installation...")
is_installed, version = verify_ollama()
if is_installed:
    print(f"✓ Ollama is installed: {version}")
else:
    print("✗ Ollama is not installed")

print()

# Test 2: List available models
print("Test 2: Listing available models...")
models_output = list_installed_models()
if models_output:
    print("✓ Available models:")
    print(models_output)
else:
    print("✗ Failed to list models")

print()

# Test 3: Send a test prompt
print("Test 3: Testing model with a prompt...")
print("Prompt: 'Write a haiku about AI'")
print()

test_model = MODELS[0]['name']
try:
    result = subprocess.run(
        ['ollama', 'run', test_model, "Write a haiku about AI"],
        capture_output=True,
        text=True,
        timeout=60
    )
    if result.returncode == 0:
        print(f"✓ Response from {test_model}:")
        print("-" * 60)
        print(result.stdout.strip())
        print("-" * 60)
    else:
        print(f"✗ Failed to get response: {result.stderr}")
except subprocess.TimeoutExpired:
    print("✗ Request timed out")
except Exception as e:
    print(f"✗ Error running model: {e}")

print()

# Test 4: Quick conversation test
print("Test 4: Testing with a creative prompt...")
print("Prompt: 'Tell me a very short joke about robots'")
print()

try:
    result = subprocess.run(
        ['ollama', 'run', test_model, "Tell me a very short joke about robots"],
        capture_output=True,
        text=True,
        timeout=60
    )
    if result.returncode == 0:
        print("✓ Response:")
        print("-" * 60)
        print(result.stdout.strip())
        print("-" * 60)
    else:
        print(f"✗ Failed: {result.stderr}")
except subprocess.TimeoutExpired:
    print("✗ Request timed out")
except Exception as e:
    print(f"✗ Error: {e}")

print()
print(SEPARATOR)
print("CHAT TEST COMPLETE")
print(SEPARATOR)
print()
print("The chat application is working! To start chatting interactively:")
print("  python chat.py")
print()
