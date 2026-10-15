import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/models"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()

if "data" in data:
    print("--- الموديلات المتاحة فعلياً لمفتاحك ---")
    for m in data["data"]:
        print(m["id"])
else:
    print("مشكلة في المفتاح أو الإجابة:", data)