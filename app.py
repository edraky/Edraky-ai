from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Ollama API is running!"}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt", "")

    # Run Ollama model (replace 'llama2' with your model)
    result = subprocess.run(
        ["ollama", "run", "llama2"],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    return jsonify({"response": result.stdout.decode().strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
