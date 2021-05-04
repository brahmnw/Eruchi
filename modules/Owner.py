import discord
from discord.ext import commands
import aiohttp
import asyncio

class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['owner', 'o'])
    @commands.is_owner()
    async def ownercommands(self, ctx):
        return

    @ownercommands.command(aliases=['l'])
    async def load(self, ctx, module):
        self.bot.load_extension(f"modules.{module}")
        await ctx.send(f":hammer: **Loaded** `{module}`!")

    @ownercommands.command(aliases=['ul'])
    async def unload(self, ctx, module):
        self.bot.unload_extension(f"modules.{module}")
        await ctx.send(f":hammer: **Unloaded** `{module}`!")

    @ownercommands.command(aliases=['rl'])
    async def reload(self, ctx, module):
        self.bot.unload_extension(f"modules.{module}")
        self.bot.load_extension(f"modules.{module}")
        await ctx.send(f":hammer: **Reloaded** `{module}`!")

    @ownercommands.command()
    async def presence(self, ctx, *, presence):
        await self.bot.change_presence(activity=discord.Game(presence))
        await ctx.send(f"Successfully changed presence to `{presence}`!")

    @ownercommands.command(aliases=['ss'])
    async def start_session(self, ctx):
        self.bot.session = aiohttp.ClientSession()
        await ctx.send(f"Started `aiohttp.ClientSession()`.")

def setup(bot):
    bot.add_cog(Owner(bot))