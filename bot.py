import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.w.',intents=intents)

@bot.event
async def on_ready():
    print(">> Meow Helo <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1037043949837221929)
    await channel.send(f'{member} 加入了!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1037043949837221929)
    await channel.send(f'{member} 離開了!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

bot.run('TOKEN')