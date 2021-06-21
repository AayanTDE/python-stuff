from discord.ext import commands

class owo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def owoify(str):
        translate = ""
        for i in str:
            if i in "RL":
                translate += "W"
            elif i in "rl":
                translate += "w"
            else:
                translate += i
        return translate

    @commands.command(name="owoify", aliases=["owo"])
    async def owoify(self, ctx, *, arg: owoify):
        await ctx.send(arg)


def setup(bot: commands.Bot):
    bot.add_cog(owo(bot))
