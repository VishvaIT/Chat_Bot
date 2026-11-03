
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


def check_ollama():

    try:
        response = requests.get(
            f"{OLLAMA_URL}/api/tags",
            timeout=2
        )

        response.raise_for_status()

        models = response.json().get("models", [])

        return any(
            model.get("name", "").split(":")[0] == MODEL
            for model in models
        )

    except requests.RequestException:
        return False


def chat_stream(messages):

    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": True,
        "keep_alive": "10m"
    }

    with requests.post(
        f"{OLLAMA_URL}/api/chat",
        json=payload,
        stream=True,
        timeout=(5, 300)
    ) as response:

        response.raise_for_status()

        for line in response.iter_lines():

            if not line:
                continue

            data = json.loads(line)

            content = data.get("message", {}).get("content", "")

            if content:
                yield content

            if data.get("done"):
                break
