from discord.ext import commands


blacklist = [466522885536612353 # sigma
]


class repeat(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="echo", aliases=["say", "repeat"])
    async def echo(self, ctx, *, arg):
        if ctx.author.id in blacklist:
            return
        await ctx.send(arg)

    @commands.command(name="shout", aliases=["scream", "yell"])
    async def shout(self, ctx, *, arg):
        if ctx.author.id in blacklist:
            return
        await ctx.send(arg.upper())

    @commands.command(name="spam")
    async def spam(self, ctx, arg, count):
        if ctx.author.id in blacklist:
            return
        elif int(count) > 100:
            await ctx.send("Too large number! 100 is the max.")
        elif "270141848000004097" in arg:
            await ctx.send("You cannot spam ping the owner!")
        elif "@everyone" in arg:
            await ctx.send("You cannot spam ping everyone!")
        else:
            for i in range(int(count)):
                await ctx.send(arg)


def setup(bot: commands.Bot):
    bot.add_cog(repeat(bot))
