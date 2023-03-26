import requests
import openai

def interact_with_chatgpt(text, api_key):
    openai.api_key=api_key
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role":"system",
                "content":"あなたの名前はPolyGlotPalです。"
            },
            {
                "role":"user",
                "content":text
            }
        ]
    )
    return response["choices"][0]["message"]["content"]
