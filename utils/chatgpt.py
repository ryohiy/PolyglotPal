import requests

def interact_with_chatgpt(text, api_key):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": text,
        "max_tokens": 50,
        "n": 1,
        "stop": None,
        "temperature": 0.8
    }
    response = requests.post(url, headers=headers, json=data)
    chatgpt_response = response.json()["choices"][0]["text"]
    return chatgpt_response.strip()
