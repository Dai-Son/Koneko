import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Pics(Cog_Extension):
    
    @commands.command()
    async def hello(self, ctx):
        pic = discord.File(jdata['hello_pic'])
        await ctx.send(file= pic)

    @commands.command()
    async def rdmpic(self, ctx):
        random_pic = random.choice(jdata['random_pic'])
        rpic = discord.File(random_pic)
        await ctx.send(file= rpic)

async def setup(bot):
    await bot.add_cog(Pics(bot))