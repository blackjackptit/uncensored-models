# GPU Optimization Guide for Ollama

## Your System

- **GPU**: NVIDIA GeForce RTX 2060 SUPER
- **VRAM**: 8 GB
- **CUDA**: Version 12.6
- **Status**: ✅ GPU acceleration ENABLED and working

## Current Performance

Ollama automatically detects and uses your NVIDIA GPU. You can verify this by running:

```bash
nvidia-smi
```

Look for `ollama.exe` in the process list - if it shows Type "C" (Compute), GPU is active.

## GPU Memory Management

Your RTX 2060 SUPER has 8GB VRAM. Here's how models fit:

### Models That Run Entirely on GPU (Best Performance)
- **dolphin-mistral:latest** (7B) - ~4GB VRAM → ✅ Full GPU
- **dolphin-llama3:latest** (8B) - ~5GB VRAM → ✅ Full GPU
- **wizardlm-uncensored:13b** - ~7GB VRAM → ✅ Full GPU

### Large Models (Partial GPU Offloading)
- **dolphin-mixtral:8x7b** (47B) - ~26GB needed → ⚠️ Hybrid (GPU + RAM)
  - Ollama will offload layers between GPU and RAM automatically
  - Still much faster than CPU-only

## Optimization Tips

### 1. Monitor GPU Usage During Inference

```bash
# Keep this running in another terminal
nvidia-smi -l 1
```

Watch the "Memory-Usage" and "GPU-Util" columns spike during model responses.

### 2. Set GPU Layers (Advanced)

By default, Ollama maximizes GPU usage. To manually control layer offloading:

```bash
# Set number of layers to offload to GPU
$env:OLLAMA_NUM_GPU=99  # Use maximum GPU layers (recommended)

# Or limit for specific cases
$env:OLLAMA_NUM_GPU=35  # Use fewer layers (if you need VRAM for other apps)
```

### 3. Optimize Context Window

Larger context windows use more VRAM:

```bash
# Default is 2048 tokens
# Reduce for more VRAM:
$env:OLLAMA_NUM_CTX=2048

# Or increase if you have VRAM to spare:
$env:OLLAMA_NUM_CTX=4096
```

### 4. Batch Size Optimization

```bash
# Increase batch size for better GPU utilization
$env:OLLAMA_NUM_BATCH=512  # Default, good for 8GB

# Reduce if you get OOM errors
$env:OLLAMA_NUM_BATCH=256
```

## Performance Benchmarks (Estimated)

With GPU acceleration on RTX 2060 SUPER:

| Model | VRAM Usage | Tokens/sec | Speed vs CPU |
|-------|-----------|------------|--------------|
| dolphin-mistral 7B | ~4 GB | 40-60 | 8-10x faster |
| dolphin-llama3 8B | ~5 GB | 35-50 | 8-10x faster |
| wizardlm-uncensored 13B | ~7 GB | 25-35 | 6-8x faster |
| dolphin-mixtral 8x7b | ~8 GB (partial) | 15-25 | 4-6x faster |

## Troubleshooting

### GPU Not Being Used?

1. **Check NVIDIA drivers**:
   ```bash
   nvidia-smi
   ```
   Should show driver version and CUDA version.

2. **Restart Ollama service**:
   ```bash
   # Stop Ollama
   taskkill /F /IM ollama.exe

   # Start Ollama (it will auto-restart)
   ollama serve
   ```

3. **Verify CUDA installation**:
   ```bash
   nvcc --version
   ```

### Out of Memory Errors

If you get OOM errors with large models:

1. **Reduce context window**:
   ```bash
   $env:OLLAMA_NUM_CTX=1024
   ```

2. **Reduce batch size**:
   ```bash
   $env:OLLAMA_NUM_BATCH=256
   ```

3. **Close other GPU applications** (browsers, games, etc.)

4. **Use smaller models** (7B/8B instead of 13B+)

### Performance Issues

1. **Check GPU temperature**:
   ```bash
   nvidia-smi
   ```
   If temp > 80°C, GPU may throttle. Improve cooling.

2. **Monitor GPU utilization**:
   - Should spike to 90-100% during inference
   - If staying low, check for CPU bottlenecks

3. **Update NVIDIA drivers**:
   - Download latest from: https://www.nvidia.com/download/index.aspx

## Best Practices

### For Maximum Speed
- Use 7B-8B models that fit entirely in VRAM
- Close other GPU-intensive applications
- Keep GPU drivers updated

### For Large Models (8x7B)
- Accept hybrid GPU+RAM mode
- Still 4-6x faster than CPU-only
- Consider upgrading to models that fit in 8GB if speed is critical

### For Development
- Use smaller models (7B) for quick iterations
- Switch to larger models (8x7B, 13B) for final testing

## Environment Variables Reference

Add these to your shell profile or set before running Ollama:

```bash
# GPU Configuration
$env:OLLAMA_NUM_GPU=99           # Max GPU layers (default: auto)
$env:OLLAMA_GPU_LAYERS=99        # Alternative name

# Memory Configuration
$env:OLLAMA_NUM_CTX=2048         # Context window size (tokens)
$env:OLLAMA_NUM_BATCH=512        # Batch size
$env:OLLAMA_NUM_THREAD=8         # CPU threads (for hybrid mode)

# Model Storage
$env:OLLAMA_MODELS=D:\llm-models # Model storage path
```

## Verification Commands

### Check GPU is Active
```bash
# During model inference, run:
nvidia-smi

# Look for:
# - ollama.exe in process list
# - High Memory-Usage (GB)
# - GPU-Util spikes to 90-100%
```

### Test GPU Performance
```bash
# Run a quick test
set OLLAMA_MODELS=D:\llm-models
ollama run dolphin-mistral:latest "Write a short poem about AI"

# Watch nvidia-smi in another terminal
# You should see GPU-Util spike to ~100% during generation
```

## Summary

✅ Your RTX 2060 SUPER is automatically being used by Ollama
✅ 7B-13B models run entirely on GPU for maximum speed
✅ Larger models use hybrid GPU+RAM (still much faster than CPU)
✅ No additional configuration needed - it just works!

For questions or issues, check the main README or open an issue on GitHub.
