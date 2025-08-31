# Ollama API on Render

This repo runs Ollama inside Docker and exposes it through a Flask API.

### Run locally
```bash
docker build -t ollama-api .
docker run -p 5000:5000 ollama-api
