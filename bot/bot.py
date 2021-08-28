import discord
from discord.ext import commands
import json
import aiohttp
import asyncio

class Eruchi(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def start(self, *args, **kwargs):
        self.session = aiohttp.ClientSession()
        await super().start(*args, **kwargs)

    async def close(self, *args, **kwargs):
        await self.session.close()
        await super().close()

loadup_cogs = [
    'base',
    'events',
    'fun',
    'games',
    'sauceroulette',
    'owner'
]

bot = Eruchi(
    command_prefix='e;',
    owner_ids=[
        154433538375024640
    ]
)

bot.remove_command('help')

if __name__ == '__main__':

    for cog in loadup_cogs:
        bot.load_extension(f"cogs.{cog}")
        
    with open('tokens.json', 'r') as f:
        bot_info = json.loads(f.read())
    
    bot.info = bot_info

    bot.run(bot_info['token'])
