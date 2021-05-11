import discord
from discord.ext import commands
import random
import json

class SauceRoulette(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sr(self, ctx):

        rarity = random.randint(1, 1000)
        category = 'common'

        #spaghetti code lol

        if rarity < 3:
            category = 'Mythical'
            color = discord.Colour.from_rgb(255, 92, 92)

        elif rarity < 20:
            category = 'Legendary'
            color = discord.Colour.from_rgb(255, 230, 0)

        elif rarity < 75:
            category = 'Epic'
            color = discord.Colour.from_rgb(219, 145, 242)

        elif rarity < 175:
            category = 'Rare'
            color = discord.Colour.from_rgb(145, 185, 242)
        
        elif rarity < 400:
            category = 'Uncommon'
            color = discord.Colour.from_rgb(145, 242, 149)

        elif rarity < 1000:
            category = 'Common'
            color = discord.Colour.from_rgb(130, 130, 130)
        
        with open(f'cmd_data/sauces/{category.lower()}.json', 'r', encoding='utf8') as f:
            jsons = json.loads(f.read())
            sauce = random.choice(jsons['list'])
            title = sauce[0]
            image = sauce[1]

        embed=discord.Embed(
            title=title,
            description=f"**Rarity:** {category}",
            colour = color
        )
        embed.set_image(url=image)
        embed.set_footer(text='Eruchi Sauce Roulette')

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(SauceRoulette(bot))
