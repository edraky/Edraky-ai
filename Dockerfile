FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl git python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Create working directory
WORKDIR /app

# Copy app
COPY . /app

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose Flask API port
EXPOSE 5000

# Run Ollama server + Flask app
CMD ollama serve & python3 app.py
