import discord
from discord.ext import commands
import random

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, size=6):
        roll = random.randint(1, size)
        embed = discord.Embed(
            color=discord.Color.blurple()
        ) \
            .set_footer(text=f"🎲 You rolled {roll}! (Out of a total of {size}).")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))
