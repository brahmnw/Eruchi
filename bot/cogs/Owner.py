import discord
from discord.ext import commands
import aiohttp
import asyncio

class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['o'], hidden=true)
    @commands.is_owner()
    async def _owner(self, ctx):
        return

    @owner.command(aliases=['l'])
    async def _load(self, ctx, module):
        self.bot.load_extension(f"cogs.{module}")
        await ctx.send(f":hammer: **Loaded** `{module}`!")

    @owner.command(aliases=['rl'])
    async def _reload(self, ctx, module):
        self.bot.reload_extension(f"cogs.{module}")
        await ctx.send(f":hammer: **Reloaded** `{module}`!")

    @owner.command()
    async def _presence(self, ctx, *, presence):
        await self.bot.change_presence(activity=discord.Game(presence))
        await ctx.send(f"Successfully changed presence to `{presence}`!")

    @owner.command(aliases=['ss'])
    async def _start_aiohttp(self, ctx):
        self.bot.session = aiohttp.ClientSession()
        await ctx.send(f"Started `aiohttp.ClientSession()`.")

def setup(bot):
    bot.add_cog(Owner(bot))