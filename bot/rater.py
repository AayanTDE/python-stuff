from discord.ext import commands

def char_to_numb(char):
    if char in "qwertyuiopasdfghjklzxcvbnm":
        return ord(char[0]) - 96
    elif char == " ":
        return 0
    else:
        return

class rater(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def rate(phrase):
        base = 0
        for i in phrase.lower():
            base += char_to_numb(i)
        return base
    @commands.command(name="rateme", aliases=["rate", "rater"])
    async def rateme(self, ctx, *, arg: rate):
        await ctx.send(f"Your rating is {arg}!")


def setup(bot: commands.Bot):
    bot.add_cog(rater(bot))
