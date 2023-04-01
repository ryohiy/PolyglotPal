import discord
from discord.ext import commands
import json
from utils import translate_japanese_to_english, translate_english_to_japanese, interact_with_chatgpt

with open("api_keys.json", "r") as f:
    api_keys = json.load(f)

polyglotpal_bot_key = api_keys["polyglotpal"]
deepl_api_key = api_keys["deepl"]
chatgpt_api_key = api_keys["chatgpt"]

# Intentsオブジェクトの作成
intents = discord.Intents.all()
client = discord.Client(intents=intents)

def ask(user_input):
    translated_input = translate_japanese_to_english(user_input, deepl_api_key)
    chatgpt_response = interact_with_chatgpt(translated_input, chatgpt_api_key)
    translated_response = translate_english_to_japanese(chatgpt_response, deepl_api_key)
    return translated_response
@client.event
async def on_message(message):
    if message.content.startswith("!ask"):
        await message.channel.send("何でも聞いて")
        wait_message = await client.wait_for("message")
        res = ask(wait_message.content)
        await message.channel.send(res)
client.run(polyglotpal_bot_key)