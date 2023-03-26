import discord
from discord.ext import commands
import json
from utils import translate_japanese_to_english, translate_english_to_japanese, interact_with_chatgpt

with open("api_keys.json", "r") as f:
    api_keys = json.load(f)

polyglotpal_bot_key = api_keys["polyglotpal"]
deepl_api_key = api_keys["deepl"]
chatgpt_api_key = api_keys["chatgpt"]

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ask(ctx, *, user_input: str):
    translated_input = translate_japanese_to_english(user_input, deepl_api_key)
    print(user_input)
    print(translated_input)
    print(chatgpt_api_key)
    chatgpt_response = interact_with_chatgpt(translated_input, chatgpt_api_key)
    print(translated_input)
    print(chatgpt_response)
    translated_response = translate_english_to_japanese(chatgpt_response, deepl_api_key)
    await ctx.send(translated_response)

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"エラーが発生しました: {str(error)}")

bot.run(polyglotpal_bot_key)
