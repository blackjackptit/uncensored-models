# Uncensored Models

A Python-based chat interface for running uncensored AI models locally using Ollama. This project provides an easy-to-use command-line interface for interacting with various uncensored language models.

## Features

- **Interactive Chat Interface**: Clean, user-friendly CLI for conversing with AI models
- **GPU Acceleration**: Automatic NVIDIA GPU support for 8-10x faster inference
- **Multiple Model Support**: Easy switching between different uncensored models
- **Conversation History**: Maintains context throughout the chat session
- **Automated Setup**: One-command setup wizard to get started quickly
- **Local & Private**: All models run locally on your machine
- **Modular Architecture**: Clean, maintainable codebase following DRY principles

## Available Models

- **Dolphin Mistral 7B** - Balanced quality and speed
- **Dolphin Llama3 8B** - High quality responses
- **WizardLM Uncensored 7B** - Instruction-tuned for better task following
- **Nous Hermes Uncensored** - Creative and conversational

## Prerequisites

- **Python 3.7+** - [Download Python](https://www.python.org/downloads/)
- **Ollama** - [Install Ollama](https://ollama.ai)
- **8-16 GB RAM** recommended for smooth model performance
- **10+ GB disk space** for model storage
- **NVIDIA GPU** (optional but recommended) - 8-10x faster with GPU acceleration
  - Automatically detected and used if available
  - See [GPU Optimization Guide](docs/GPU_OPTIMIZATION.md) for details

## Installation

1. Clone this repository:
\`\`\`bash
git clone https://github.com/blackjackptit/uncensored-models.git
cd uncensored-models
\`\`\`

2. Install Ollama if you haven't already:
   - Visit https://ollama.ai and follow the installation instructions for your OS

3. Run the setup wizard:
\`\`\`bash
python setup_ollama.py
\`\`\`

The setup wizard will:
- Configure the model storage directory
- Download your selected models
- Verify the installation

## Usage

### Start Chatting

\`\`\`bash
python chat.py
\`\`\`

### Chat Commands

While in the chat interface, you can use these commands:

- \`/clear\` - Clear conversation history
- \`/model\` - Switch to a different model
- \`/exit\` or \`/quit\` - Exit the chat

### Running Tests

\`\`\`bash
python test_chat.py
\`\`\`

## Project Structure

\`\`\`
uncensored-models/
├── config.py           # Configuration settings and model definitions
├── ollama_utils.py     # Shared utility functions for Ollama operations
├── setup_ollama.py     # One-time setup wizard
├── chat.py             # Interactive chat application
├── test_chat.py        # Automated test suite
├── requirements.txt    # Python dependencies (minimal)
├── docs/
│   └── DEVELOPMENT.md  # Developer documentation
└── README.md           # This file
\`\`\`

## Configuration

Edit \`config.py\` to customize:

- **MODEL_DIR**: Where models are stored (default: \`D:/llm-models\`)
- **MODELS**: Add or remove models from the available list

Example of adding a new model:
\`\`\`python
MODELS.append({
    'name': 'model-identifier',
    'description': 'Display Name',
    'details': 'Brief description'
})
\`\`\`

## Development

For detailed development documentation, see [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md).

### Quick Start for Developers

1. Read the architecture overview in \`docs/DEVELOPMENT.md\`
2. Follow the code style guidelines (Google-style docstrings)
3. Test your changes with \`python test_chat.py\`
4. One feature per commit with descriptive messages

## Performance Notes

### GPU Acceleration (Recommended)
- **NVIDIA GPU automatically detected and used** - no configuration needed
- **8-10x faster** inference with GPU vs CPU-only
- RTX 2060 SUPER or better recommended
- See [GPU Optimization Guide](docs/GPU_OPTIMIZATION.md) for advanced tuning

### General Performance
- Each model is approximately 4-7 GB in size
- Models are downloaded sequentially during setup
- Use \`/clear\` command in long conversations to manage memory
- First response after loading a model may be slower

### Expected Performance (with GPU)
- **7B models**: 40-60 tokens/second
- **8B models**: 35-50 tokens/second
- **13B models**: 25-35 tokens/second
- **8x7B models**: 15-25 tokens/second

## Security & Responsible Use

- All models run locally without internet connectivity during inference
- No data is sent to external servers
- These are uncensored models - users are responsible for appropriate use
- Follow local laws and regulations regarding AI usage

## Troubleshooting

**Ollama not found:**
- Verify Ollama is installed: \`ollama --version\`
- Check that Ollama is in your system PATH

**Model not found:**
- Run \`python setup_ollama.py\` again to download models
- Check that OLLAMA_MODELS environment variable points to correct directory

**Import errors:**
- Ensure all \`.py\` files are in the same directory
- Verify Python 3.7+ is installed: \`python --version\`

**High memory usage:**
- These models require 8-16 GB RAM
- Close other applications if experiencing slowdowns
- Use smaller models like Dolphin Mistral for lower memory usage

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (\`git checkout -b feature/amazing-feature\`)
3. Follow the code style in \`docs/DEVELOPMENT.md\`
4. Test thoroughly with \`test_chat.py\`
5. Commit your changes (\`git commit -m 'feat: add amazing feature'\`)
6. Push to the branch (\`git push origin feature/amazing-feature\`)
7. Open a Pull Request

## License

This project is provided as-is for educational and research purposes. Users are responsible for compliance with applicable laws and Ollama's terms of service.

## Acknowledgments

- Built on [Ollama](https://github.com/ollama/ollama) - Local LLM runtime
- Models by various creators in the open-source AI community

## Support

For issues and questions:
- Open an issue on [GitHub](https://github.com/blackjackptit/uncensored-models/issues)
- Check existing issues for solutions
- Review \`docs/DEVELOPMENT.md\` for technical details

---

**Note**: This project facilitates running uncensored AI models. Use responsibly and in accordance with your local laws and ethical guidelines.
