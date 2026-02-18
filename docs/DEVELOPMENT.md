# Developer Documentation

## Architecture

```
config.py (Configuration)
    ↓ imported by
ollama_utils.py (Shared Functions)
    ↓ imported by
setup_ollama.py | chat.py | test_chat.py (Applications)
```

**Design Principles**: DRY (no duplication), Single Responsibility, Modularity

**Modules**:
- `config.py` - MODEL_DIR, MODELS list, SEPARATOR constant
- `ollama_utils.py` - 7 functions for Ollama operations (see inline docs)
- `setup_ollama.py` - One-time setup wizard
- `chat.py` - Interactive chat with conversation history
- `test_chat.py` - Automated validation suite

## Quick Reference

### Add a Model
Edit `config.py`:
```python
MODELS.append({
    'name': 'model-identifier',
    'description': 'Display Name',
    'details': 'Brief description'
})
```

### Add a Utility Function
Add to `ollama_utils.py` with Google-style docstring, then import where needed.

### Add a Chat Command
Edit `chat.py` in the `chat()` function:
```python
if user_input == '/command':
    # handle command
    continue
```

## Code Style

**Docstrings**: Google-style with Args, Returns, Example
**Imports**: stdlib → third-party → local
**Errors**: Try-except with user-friendly messages (✓/✗ prefix)
**UI**: Use SEPARATOR constant, keep output clean

**Example**:
```python
def function(param):
    """Brief description.

    Args:
        param (type): Description

    Returns:
        type: Description
    """
    try:
        result = operation()
        return result.returncode == 0
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
```

## Testing

**Before Committing**:
```bash
python setup_ollama.py  # Run once
python test_chat.py     # All tests pass
python chat.py          # Test model selection, messages, commands
```

**Common Issues**:
- Import errors → Check all .py files in same directory
- Ollama not found → Verify PATH, try `ollama --version`
- Models not found → Check OLLAMA_MODELS env var

**Add Test**: Append to `test_chat.py` with try-except and ✓/✗ output

## Performance & Security

**Performance**:
- Models: 4-7 GB each, sequential downloads
- Chat: History concatenates, use `/clear` for long conversations
- Memory: 8-16 GB RAM per model

**Security**:
- No `shell=True` in subprocess calls
- OLLAMA_MODELS directory should have proper permissions
- Uncensored models → users responsible for appropriate use

## Contributing

1. Read this doc, understand architecture
2. One feature per commit
3. Update docs with code
4. Test thoroughly (see Testing above)
5. Follow code style

**Commit Format**: `<type>: <subject>` where type = feat|fix|docs|refactor|test|chore

**Code Review Checklist**:
- [ ] Follows style guidelines
- [ ] Has docstrings
- [ ] Docs updated
- [ ] No hardcoded values (use config.py)
- [ ] No duplication
- [ ] Tests pass

## Troubleshooting

**Module not found**: Verify files in same directory: `python -c "import config"`

**Ollama API changes**: Update `ollama_utils.py` functions, test, update docs

**Model compatibility**: Different context windows/formats, test with `test_chat.py`

## Distribution

Pure Python, no build required.

```bash
# Package
zip -r uncensored-models.zip *.py *.md *.txt docs/

# Deploy
# 1. Extract, 2. Install Python 3.7+ and Ollama, 3. Run setup_ollama.py
```

## Future Plans

- [ ] Conversation save/load
- [ ] Custom system prompts
- [ ] Streaming responses
- [ ] Logging module
- [ ] Plugin system

## Resources

- [Ollama Docs](https://github.com/ollama/ollama)
- [Python subprocess](https://docs.python.org/3/library/subprocess.html)
- [Google Style Guide](https://google.github.io/styleguide/pyguide.html)
