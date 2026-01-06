"""Simple test script to verify the API is working."""

import requests
import json

BASE_URL = "http://localhost:8000"


def test_root():
    """Test root endpoint."""
    print("Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()


def test_health():
    """Test health check endpoint."""
    print("Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    print()


def test_models():
    """Test list models endpoint."""
    print("Testing list models endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/llm/models")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    print()


def test_generate():
    """Test text generation endpoint."""
    print("Testing generate endpoint...")
    try:
        payload = {
            "prompt": "What is an AI agent? Answer in one sentence.",
            "stream": False,
            "think": False
        }
        response = requests.post(
            f"{BASE_URL}/llm/generate",
            json=payload
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    print()


if __name__ == "__main__":
    print("=" * 60)
    print("API Test Suite")
    print("=" * 60)
    print()

    print("Make sure:")
    print("1. Ollama is running (ollama ps)")
    print("2. API is running (python run.py)")
    print("3. You have at least one model pulled")
    print()
    print("=" * 60)
    print()

    test_root()
    test_health()
    test_models()
    test_generate()

    print("=" * 60)
    print("Tests complete!")
    print("=" * 60)
