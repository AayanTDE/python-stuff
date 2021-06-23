import random
from discord.ext import commands


class rand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="rps", aliases=["rockpaperscissors"])
    async def rps(self, ctx, user):
        cpu = random.choice(["r", "p", "s"])
        if user == cpu:
            await ctx.send("Tie!")
        elif user == "r":
            if cpu == "p":
                await ctx.send("CPU picked paper so you lost!")
            else:
                await ctx.send("CPU picked scissors so you won!")
        elif user == "p":
            if cpu == "r":
                await ctx.send("CPU picked rock so you won!")
            else:
                await ctx.send("CPU picked scissors so you lost!")
        elif user == "s":
            if cpu == "r":
                await ctx.send("CPU picked rock so you lost!")
            else:
                await ctx.send("CPU picked paper so you won!")
        else:
            await ctx.send("You were supposed to enter either r, p, or s!")

    @commands.command(name="coinflip", aliases=["ht", "flip"])
    async def coinflip(self, ctx):
        coin = random.randint(1, 2)
        if coin == 1:
            await ctx.send("Heads!")
        else:
            await ctx.send("Tails!")


def setup(bot: commands.Bot):
    bot.add_cog(rand(bot))
