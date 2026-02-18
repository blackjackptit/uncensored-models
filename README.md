# Uncensored LLM Chat

A modular command-line chat interface for uncensored language models using Ollama.

## Quick Start

```bash
# 1. Install Ollama from https://ollama.ai
# 2. Run setup
python setup_ollama.py
# 3. Start chatting
python chat.py
```

## Features

- 4 uncensored models: Dolphin Mistral, Dolphin Llama3, WizardLM, Nous Hermes
- Interactive CLI with conversation history
- Runtime model switching
- Modular, maintainable codebase

## Installation

### Requirements
- Python 3.7+
- Ollama ([download](https://ollama.ai))
- ~20 GB disk space for all models

### Setup

1. **Install Ollama**
   Download from [https://ollama.ai](https://ollama.ai) and run the installer.

2. **(Optional) Configure Custom Model Directory**

   To store models in `D:\llm-models`, set the environment variable:

   **PowerShell (Administrator):**
   ```powershell
   [System.Environment]::SetEnvironmentVariable("OLLAMA_MODELS", "D:\llm-models", "Machine")
   ```

   **Command Prompt (Administrator):**
   ```cmd
   setx OLLAMA_MODELS "D:\llm-models" /M
   ```

   Then restart Ollama service (end process in Task Manager, it will auto-restart).

3. **Run Setup Script**
   ```bash
   python setup_ollama.py
   ```
   This will download all models and configure the environment.

## Usage

### Start Chat
```bash
python chat.py
```

### Chat Commands
- `exit` or `quit` - Exit the application
- `/clear` - Clear conversation history
- `/models` - Switch to a different model

### Run Tests
```bash
python test_chat.py
```

## Available Models

| Model | Size | Description |
|-------|------|-------------|
| Dolphin Mistral 7B | ~4 GB | Balanced quality and speed |
| Dolphin Llama3 8B | ~5 GB | High quality responses |
| WizardLM Uncensored 7B | ~7 GB | Instruction-tuned |
| Nous Hermes Uncensored | ~4 GB | Creative responses |

**Storage**: Models are stored in `D:\llm-models` (configurable)
**RAM Requirements**: 8-16 GB per model

## Troubleshooting

**Ollama not found**
- Ensure Ollama is installed and PATH is configured
- Restart terminal after installation

**Models not downloading to custom directory**
- Verify OLLAMA_MODELS environment variable is set
- Restart Ollama service after setting the variable

**Out of memory errors**
- Close other applications
- Use smaller models (Dolphin Mistral)

**Import errors**
- Ensure all .py files are in the same directory
- Check Python version is 3.7+

## Project Structure

```
uncensored-models/
├── config.py           # Configuration
├── ollama_utils.py     # Shared utilities
├── setup_ollama.py     # Setup script
├── chat.py             # Chat interface
├── test_chat.py        # Testing suite
├── README.md           # This file
└── docs/
    └── DEVELOPMENT.md  # Developer documentation
```

## For Developers

See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for:
- Architecture and design decisions
- Adding new models and features
- Code style guidelines
- Contributing guidelines

## Responsible Use

These models have reduced content filtering compared to mainstream models. Intended for:
- Creative writing and roleplay
- Research and educational purposes
- Testing and development

Use responsibly and in accordance with local laws and regulations.

## License

This is a personal project for interfacing with Ollama. Ollama and the language models have their own licenses.
