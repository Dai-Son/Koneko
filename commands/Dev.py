import discord
from discord.ext import commands
from core.classes import Cog_Extension 

class Dev(Cog_Extension):
    @commands.command()
    async def load(self, ctx, extension):
        await self.bot.load_extension(f'commands.{extension}')
        await ctx.send(f'已加載 {extension}!')

    @commands.command()
    async def unload(self, ctx, extension):
        await self.bot.unload_extension(f'commands.{extension}')
        await ctx.send(f'已卸載 {extension}!')

    @commands.command()
    async def reload(self, ctx, extension):
        await self.bot.reload_extension(f'commands.{extension}')
        await ctx.send(f'已重新載入 {extension}!')

async def setup(bot):
    await bot.add_cog(Dev(bot))