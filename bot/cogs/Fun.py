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
    async def sus(self, ctx, mention: discord.User=None):

        if mention is None:
            mention = ctx.author

        sus_percent = random.randint(1, 100)

        color = discord.Colour.red()
        title = 'title messed'
        image = 'https://static.wikia.nocookie.net/jerma-lore/images/e/e3/JermaSus.jpg/revision/latest/top-crop/width/360/height/450?cb=20201206225609'

        if sus_percent == 100:
            title = 'Eatingkay'
            color = discord.Colour.red()
            image = 'https://images-ext-1.discordapp.net/external/unlixwprZJau-4Gph3mQDci7phs3tlLYDlKtINxIYMc/%3Fsize%3D256/https/cdn.discordapp.com/avatars/495351724890914816/36d61ca6bb407ba6734a5c99cd200473.png'

        elif sus_percent >= 97:
            title = 'Voted Off'
            color = discord.Colour.from_rgb(255, 52, 38)
            image = 'https://static.wikia.nocookie.net/jerma-lore/images/e/e3/JermaSus.jpg/revision/latest/top-crop/width/360/height/450?cb=20201206225609'

        elif sus_percent >= 85:
            title = 'Impostor'
            color = discord.Colour.from_rgb(232, 74, 74)
            image = 'https://www.nme.com/wp-content/uploads/2020/10/Among-Us-2.jpg' 

        elif sus_percent >= 60:
            title = 'Suspicious'
            color = discord.Colour.from_rgb(232, 148, 74)
            image = 'https://i.pinimg.com/originals/1f/19/11/1f19111ab93fe854d7e90732e730b206.png'

        elif sus_percent >= 40:
            title = 'Neutral'
            color = discord.Colour.from_rgb(235, 228, 155)
            image = 'https://i.redd.it/w0lmb8i7odo51.png'

        elif sus_percent >= 15:
            title = 'Crewmate'
            color = discord.Colour.from_rgb(195, 235, 155)
            image = 'https://3pdl3hx2mke473cw1llvz5pz-wpengine.netdna-ssl.com/wp-content/uploads/2013/09/Talk-Like-a-Pirate-Day-at-Cannons-Marina-925x1024.jpg'

        elif sus_percent >= 3:
            title = 'Medbay Scanned'
            color = discord.Colour.from_rgb(158, 235, 155)
            image = 'https://i.pinimg.com/736x/7e/e3/c0/7ee3c076f10c634ccf8cae95e94f4804.jpg'

        elif sus_percent >= 0:
            title = 'Geronimo Stilton'
            color = discord.Colour.from_rgb(77, 255, 54)
            image = 'https://i.pinimg.com/originals/fe/2c/9a/fe2c9a6ee42e9da3a058a96c11c2a8a8.png'

        embed = discord.Embed(
            title = f"<:sus:814375564889948160> {title}",
            description = f"**{mention.display_name}** is {sus_percent}% suspicious.",
            color = color
        ) \
            .set_footer(text='Official Suspicious Test.') \
            .set_thumbnail(url=image)
        
        await ctx.send(
            mention.mention,
            embed=embed
        )


def setup(bot):
    bot.add_cog(Fun(bot))
