import requests
import json
from dotenv import load_dotenv
import os

def commentProfanity(text):
    load_dotenv('.env')
    api_key = os.getenv('OPENAI_API_KEY')
    organization_key = os.getenv('OPENAI_ORG_KEY')
    url = "https://api.openai.com/v1/chat/completions"


    headers = {
        "Authorization": f"Bearer {api_key}",
        "OpenAI-Organization": organization_key,
        "Content-Type": "application/json"
    }

    text = 'Ashad is a bitch'
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Reply in one word."},
            {"role": "user", "content": f"Determine if the given text is safe or not by evaluating if it is profane, NSFW, inappropriate, or offensive. Return the value of 'safe' as either true or false in a single token: true or false. Text:{text}"}
        ],
        "max_tokens": 1
    }
    json_data = json.dumps(data)
    response = requests.post(url, headers=headers, data=json_data)
    response_data = response.json()


    # response = requests.post(url, headers=headers, json=data)

    # Check response status code
    if response.status_code == 200:
        # Authentication successful
        print("Authentication successful")
        reply = response_data["choices"][0]["message"]["content"]
        safe = reply.lower()
        if (safe != "true" or safe != "false"):
            safe = "false"
        print(safe)

    else:
        # Authentication failed
        print("Authentication failed")
        print("Request failed:", response.text)
