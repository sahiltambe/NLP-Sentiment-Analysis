import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
print(f"API Key loaded: {api_key[:10]}..." if api_key else "No API key found")

# Test HTTP request to Groq API
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "llama-3.1-8b-instant",
    "messages": [{"role": "user", "content": "Say hello"}],
    "max_tokens": 10,
    "temperature": 0.1
}

try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    result = response.json()
    print("✓ API call successful")
    print(f"Response: {result['choices'][0]['message']['content']}")
except Exception as e:
    print(f"✗ API call failed: {e}")
    if hasattr(e, 'response'):
        print(f"Status code: {e.response.status_code}")
        print(f"Response: {e.response.text}")