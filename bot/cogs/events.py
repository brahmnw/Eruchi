import discord
from discord.ext import commands
from discord.ext.commands import Cog
import traceback

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):  
        print('Connected to Discord and ready.')
        print(f'Currently in {len(self.bot.guilds)} guilds.')
        await self.bot.change_presence(activity=discord.Game("whats good"))
        
    @Cog.listener()
    async def on_command_error(self, ctx, exception):

        ignore_errors = [
            commands.CommandNotFound,
            commands.NotOwner
        ]

        for error in ignore_errors:

            if isinstance(exception, error):
                return

        if isinstance(exception, commands.MissingRequiredArgument):

            await ctx.send(
                embed=discord.Embed(
                    color=discord.Colour.red()
                ) \
                    .set_footer(text="🚫 Your command is missing a required argument.")
            )

        else:

            print(f"[COMMAND EXCEPTION] {exception}")

            await ctx.send(
                embed=discord.Embed(
                    color=discord.Colour.red()
                ) \
                    .set_footer(text="🚫 An unknown error has occurred. A report was sent to the command console.")
            )


def setup(bot):
    bot.add_cog(Events(bot))
