import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
print("ENV FILE FOUND:", os.path.exists(".env"))

if not OPENROUTER_API_KEY:
    print("API Key is missing. Please check your .env file.")
    exit(1)  # Exit the program if the API key is not found

def chat_with_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "X-Title": "AI Bot Python CLI",
    }
    payload = {
        "model": "nousresearch/deephermes-3-mistral-24b-preview:free",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)

    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    else:
        return f"[ERROR {response.status_code}] {response.text}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_openrouter(user_input)
        print("Chatbot:", response)
