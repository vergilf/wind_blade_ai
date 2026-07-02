import requests

url = "http://localhost:1234/v1/chat/completions"

payload = {
    "model": "local-model",
    "messages": [
        {
            "role": "user",
            "content": "Hello! Please introduce yourself in one sentence."
        }
    ],
    "temperature": 0.2,
    "max_tokens": 100
}

response = requests.post(url, json=payload, timeout=30)

print("Status Code:", response.status_code)
print(response.json())