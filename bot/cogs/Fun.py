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

    @commands.command()
    async def sus(self, ctx, mention: discord.User):

        sus_percent = random.randint(1, 100)

        color = discord.Colour.gold()

        if sus_percent >= 90:
            color = discord.Colour.from_rgb(240, 112, 103)

        elif sus_percent >= 75:
            color = discord.Colour.from_rgb(240, 174, 103)

        elif sus_percent >= 50:
            color = discord.Colour.from_rgb(235, 228, 155)

        elif sus_percent >= 25:
            color = discord.Colour.from_rgb(195, 235, 155)

        elif sus_percent >= 0:
            color = discord.Colour.from_rgb(158, 235, 155)

        embed = discord.Embed(
            description = f"<:sus:814375564889948160> {mention.display_name} is {sus_percent}% suspicious!!",
            color = color
        )
        
        await ctx.send(
            mention.mention,
            embed=embed
        )


def setup(bot):
    bot.add_cog(Fun(bot))
