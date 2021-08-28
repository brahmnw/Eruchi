import discord
from discord.ext import commands
from saucenao_api import SauceNao

class Sauce(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def saucenao(self, ctx, url, index=1):
        list_index = index - 1

        get_sauce = SauceNao(api_key=self.bot.info['saucenao_key']).from_url(url)
        sauce=get_sauce[list_index]
        emb = discord.Embed(
            title=sauce.title,
            description="Retrieved using SauceNAO API"
        )

        emb.add_field(name='Artist', value=f"{sauce.author}")
        emb.add_field(name='Similarity', value=f"{sauce.similarity}%")
        if 'source' in sauce.raw['data']:
            emb.add_field(name='Source (if Applicable)', value=f"[Open Image]({sauce.raw['data']['source']})")
        else:
            emb.add_field(name='Source (if Applicable)', value=f"*No Link Found*")
        emb.add_field(name='Extra Links', value=f"\n".join(sauce.urls))
        emb.set_image(url=sauce.thumbnail)
        emb.set_footer(text=f'Showing Result {index} of {len(get_sauce)}')

        await ctx.send(embed=emb)
        

def setup(bot):
    bot.add_cog(Sauce(bot))

