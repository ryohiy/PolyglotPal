import requests

def translate_japanese_to_english(text, api_key):
    url = "https://api-free.deepl.com/v2/translate"
    data = {
        "auth_key": api_key,
        "text": text,
        "source_lang": "JA",
        "target_lang": "EN",
    }
    response = requests.post(url, data=data)
    return response.json()["translations"][0]["text"]

def translate_english_to_japanese(text, api_key):
    url = "https://api-free.deepl.com/v2/translate"
    data = {
        "auth_key": api_key,
        "text": text,
        "source_lang": "EN",
        "target_lang": "JA",
    }
    response = requests.post(url, data=data)
    return response.json()["translations"][0]["text"]
