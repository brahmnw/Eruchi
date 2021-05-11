import discord
from discord.ext import commands

from .util.profile_handler import ProfileHandler


class Profile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['me'])
    async def profile(self, ctx, member: discord.User=None):

        if ctx.invoked_subcommand is not None:
            pass

        else:

            if member == None:
                member = ctx.author
                member_id = ctx.author.id

            member_id = member.id

            ph = ProfileHandler(member_id, member)
            values = ph.get()
            color = discord.Colour.from_rgb(values['profile']['color'][0], values['profile']['color'][1], values['profile']['color'][2])
            embed = discord.Embed(
                title=member.name,
                description=values['profile']['bio'],
                colour = color
            ) \
                .set_thumbnail(url=values['profile']['avatar'])
            
            if len(values['profile']['links']) < 1:
                live_links = ['No links provided.']

            else:
                links = values['profile']['links']
                live_links = []
                for link in links:
                    live_links.append(f'[{link[0]}]({link[1]})')

            embed.add_field(name="Links", value='\n'.join(live_links))
            embed.add_field(name="Discriminator", value=f'#{member.discriminator}')
            embed.set_footer(text=f'ID: {member.id}')
                                    
            await ctx.send(embed=embed)

    @commands.group(aliases=['u'])
    async def user(self, ctx):
        pass

    @user.command()
    async def edit(self, ctx, attribute, *, value):
        ph = ProfileHandler(ctx.author.id, ctx.author)
        
        attributes = [
            'avatar',
            'bio'
        ]

        if attribute in attributes:

            ph.edit(attribute, value)
            embed=discord.Embed(
                color=discord.Colour.green()
            ) \
                .set_footer(text="✅ Done!")

            await ctx.send(embed=embed)

        else:

            embed=discord.Embed(
                color=discord.Colour.red()
            ) \
                .set_footer(text="🚫 You provided an invalid attribute. Valid attributes are available through the wiki in !help.")

            await ctx.send(embed=embed)

    @user.command()
    async def color(self, ctx, r: int, g: int, b: int):
        ph = ProfileHandler(ctx.author.id, ctx.author)

        if r > 255 or g > 255 or b > 255 or r < 1 or g < 1 or b < 1:

            embed=discord.Embed(
                color=discord.Colour.red()
            ) \
                .set_footer(text="🚫 RGB values should be between 1 and 255.")

            await ctx.send(embed=embed)
        
        else:

            colors = [r, g, b]
            ph.edit('color', colors)

            embed=discord.Embed(
                color=discord.Colour.green()
            ) \
                .set_footer(text="✅ Done!")

            await ctx.send(embed=embed)

    @commands.group()
    async def links(self, ctx):
        pass

    @links.command()
    async def add(self, ctx, title, *, url):

        ph = ProfileHandler(ctx.author.id, ctx.author)
        ph.add_link(title, url)

        embed=discord.Embed(
            color=discord.Colour.green()
        ) \
            .set_footer(text="✅ Done!")

        await ctx.send(embed=embed)

    @links.command()
    async def remove(self, ctx, title):
        
        ph = ProfileHandler(ctx.author.id, ctx.author)
        ph.remove_link(title)

        embed=discord.Embed(
            color=discord.Colour.green()
        ) \
            .set_footer(text="✅ Done!")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Profile(bot))
