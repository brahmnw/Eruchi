import discord
from discord.ext import commands

class Base(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['info', 'invite', 'support'])
    async def help(self, ctx):
        embed = discord.Embed(
            title='Eruchi',
            description='uh yeah they call me rappa 3000 and ill tell you the story of freddy fazbear pizza',
            color=discord.Colour.from_rgb(77, 157, 255)
        ) \
            .set_thumbnail(url='https://i.imgur.com/CRCB3Hr.png') \
            .add_field(name="Important Links", value="""
[Wiki](https://github.com/MrBrahm/Eruchi/wiki)
[Commands](https://github.com/MrBrahm/Eruchi/wiki/Commands)
[Github](https://github.com/MrBrahm/Eruchi)
[Support Server](https://discord.gg/QN4KfD4zsc)
            """) \
            .add_field(name="Servers", value=len(self.bot.user.guilds))
            .set_footer(text=f'Made by Brahm#8516 | ID: {self.bot.user.id}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Base(bot))
