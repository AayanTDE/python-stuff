import random
from discord.ext import commands

class trolling(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name="howmuchtrolling", aliases=["hmt", "trolling", "troll"])
    async def howmuchtrolling(self, ctx):
        trollage = random.randint(1, 100)
        await ctx.send("We do a considerable amount of trolling; " + str(trollage) + " to be exact.")


def setup(bot: commands.Bot):
    bot.add_cog(trolling(bot))
