import discord
from discord.ext import commands
import asyncio

class Games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.standard_conversion = {
            '1️⃣': '1',
            '2️⃣': '2',
            '3️⃣': '3',
            '4️⃣': '4',
            '5️⃣': '5',
            '6️⃣': '6',
            '7️⃣': '7',
            '8️⃣': '8',
            '9️⃣': '9'
        }

    def xo_generate_board(self, current_board=None, coord=None, letter=None):
        
        # make an emoji board
        self.standard_board = {
            '1': ':one:',
            '2': ':two:',
            '3': ':three:',
            '4': ':four:',
            '5': ':five:',
            '6': ':six:',
            '7': ':seven:',
            '8': ':eight:',
            '9': ':nine:'
        }
        gboard = self.standard_board

        # replace options
        if current_board is not None:
            gboard = current_board
            
            # make sure you aren't replacing someone else's sign.
            if self.standard_board[coord] == gboard[coord]:
                pass

            else:
                return None

        # if there is an input
        if coord is not None and letter is not None:
            gboard[coord] = letter
            
        board_text = f"{gboard['1']} {gboard['2']} {gboard['3']}\n{gboard['4']} {gboard['5']} {gboard['6']}\n{gboard['7']} {gboard['8']} {gboard['9']}"
        return board_text, gboard

    def xo_check_win(self, ctx, board):
        winning_combos = [
            [board['1'], board['2'], board['3']],
            [board['4'], board['5'], board['6']],
            [board['7'], board['8'], board['9']],
            [board['1'], board['4'], board['7']],
            [board['2'], board['5'], board['8']],
            [board['3'], board['6'], board['9']],
            [board['1'], board['5'], board['9']],
            [board['3'], board['5'], board['7']],
        ]

        for combo in winning_combos:
            a = combo[0]
            b = combo[1]
            c = combo[2]
            
            if a == b == c:
                return a

        return None


    async def xo_main(self, ctx, opponent, message):

        # add the reactions
        await message.clear_reactions()

        i = 0
        while i < 9:
            await message.add_reaction('{}\N{variation selector-16}\N{combining enclosing keycap}'.format(i+1))
            i = i + 1

        # generate empty board
        live_board = self.xo_generate_board()
        game_state = 0
        embed = discord.Embed(
            description=live_board[0],
            color=discord.Colour.blue()
        )

        turn = 1
        while game_state == 0:
          
            if turn == 1:
                turn_owner = ctx.author
                letter = ':x:'

            if turn == 2:
                turn_owner = opponent
                letter = ':o:'

            def check(reaction, user):
                possible_entries = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣"]

                for i in possible_entries:
                    if str(reaction.emoji) == i:
                        return turn_owner == user
            
            await message.edit(content=None, embed=embed.set_footer(text=f"🎲 You have 20 seconds to make your move, {turn_owner.display_name}!"))
            
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=check)

            except asyncio.exceptions.TimeoutError:
                if turn == 1:
                    winner = opponent
                    await message.edit(content=None, embed=discord.Embed().set_footer(text=f"🏆 {winner.display_name} won by timeout!"))
                    await message.clear_reactions()
                    return

                if turn == 2:
                    winner = ctx.author
                    await message.edit(content=None, embed=discord.Embed().set_footer(text=f"🏆 {winner.display_name} won by timeout!"))
                    await message.clear_reactions()
                    return

            real_coord = self.standard_conversion[str(reaction.emoji)]
            await reaction.remove(user)

            if turn == 1:
                new_board = self.xo_generate_board(live_board[1], coord=real_coord, letter=':x:')

                if new_board is not None:
                    live_board = new_board
                    turn = 2

                else:
                    turn = 1

            elif turn == 2:
                new_board = self.xo_generate_board(live_board[1], coord=real_coord, letter=':o:')
                if new_board is not None:
                    live_board = new_board
                    turn = 1

                else:
                    turn = 2

            embed = discord.Embed(
                description=live_board[0],
                color=discord.Colour.blue()
            )

            win_con = self.xo_check_win(ctx, live_board[1])

            if win_con == ':x:':
                winner = ctx.author
                await message.edit(embed=embed.set_footer(text=f"🏆 {winner.display_name} (❌) won the game!"))
                await message.clear_reactions()
                game_state = 1

            elif win_con == ':o:':
                winner = opponent
                await message.edit(embed=embed.set_footer(text=f"🏆 {winner.display_name} (⭕) won the game!"))
                await message.clear_reactions()
                game_state = 1

            

    @commands.group(aliases=['p'])
    async def play(self, ctx):
        pass

    @play.command(aliases=['ttt', 'nac', 'noughtsandcrosses', 'xo', 'xando'])
    async def tictactoe(self, ctx, opponent: discord.User):

        if opponent == self.bot.user:
            await ctx.send("ur too shit to fight me")
            return
        
        elif opponent == ctx.author:
            await ctx.send("fuckin loser get friends to play with jesus")
            return

        # send out the invite
        invite = await ctx.send(
            f"{opponent.mention}",
            embed=discord.Embed(
                color=discord.Color.green()
            ) \
                .set_footer(text=f"🎮 {ctx.author.display_name} has invited you to play a game of TicTacToe! You have 90 seconds to accept the invite.")
        )

        def check(reaction, user):
            return user == opponent and str(reaction.emoji) == '✅'
        
        await invite.add_reaction('✅')

        # wait for response
        try: 
            reaction, user = await self.bot.wait_for('reaction_add', timeout=90.0, check=check)
        
        except asyncio.exceptions.TimeoutError:

            await invite.edit(
                embed=discord.Embed(
                    color=discord.Color.red()
                ) \
                    .set_footer(text=f"🎮 {opponent.display_name} has failed to react to the invite within 90 seconds.")
            )
            return

        else:

            await invite.edit(
                embed=discord.Embed(
                    color=discord.Color.gold()
                ) \
                    .set_footer(text=f"🎮 Loading game...")
            )

            await self.xo_main(ctx, opponent, invite)


def setup(bot):
    bot.add_cog(Games(bot))
