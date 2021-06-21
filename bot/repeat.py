from discord.ext import commands


blacklist = [466522885536612353 # sigma
]

def upper(arg):
        return arg.upper()

class repeat(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="echo", aliases=["say", "repeat"])
    async def echo(self, ctx, *, arg):
        if ctx.author.id in blacklist:
            return
        await ctx.send(arg)

    @commands.command(name="shout", aliases=["scream", "yell"])
    async def shout(self, ctx, *, arg: upper):
        if ctx.author.id in blacklist:
            return
        await ctx.send(arg)

    @commands.command(name="spam")
    async def spam(self, ctx, arg, count):
        await ctx.send(arg * int(count))


def setup(bot: commands.Bot):
    bot.add_cog(repeat(bot))
