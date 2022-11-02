import asyncio
import discord
from discord.ext import commands
import json
import random
import os

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.w.',intents=intents)

@bot.event
async def on_ready():
    print(">> Meow Hello <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Test_Channel']))
    await channel.send(f'{member} 加入了!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Test_Channel']))
    await channel.send(f'{member} 離開了!')

async def load():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')

async def main():
    await load()
    await bot.start(jdata['TOKEN'])

asyncio.run(main())