import discord
from discord.ext import commands
from discord.ext.commands import Cog

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):  
        print('Connected to Discord and ready.')
        print(f'Currently in {len(self.bot.guilds)} guilds.')
        await self.bot.change_presence(activity=discord.Game("chitanda :)"))

def setup(bot):
    bot.add_cog(Events(bot))