from discord import Member
from discord.ext import commands
from util.shit import lyrics

blacklist = [
    466522885536612353  # sigma
]
whitelist = [
    270141848000004097,  # me
    464395887179726850,  # sandal
    412201321148710912,  # fwello
    356434749700571141,  # narv
]


class Repeat(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="echo", aliases=["say", "repeat"])
    async def echo(self, ctx, *, arg):
        if ctx.author.id in blacklist:
            return
        await ctx.send(arg)

    @commands.command(name="dsay")
    async def dsay(self, ctx, *, arg):
        await ctx.message.delete()
        await ctx.send(arg)

    @commands.command(name="shout", aliases=["scream", "yell"])
    async def shout(self, ctx, *, arg):
        if ctx.author.id in blacklist:
            return
        await ctx.send(arg.upper())

    @commands.command(name="pm")
    @commands.is_owner()
    async def pm(self, ctx, user: Member, *, message):
        await user.send(message)
        await ctx.send(f"Message sent to {user.mention} successfully\nMessage: `{message}`")

    @commands.command(name="Obie", aliases=["obie"])
    async def Obie(self, ctx):
        for i in lyrics:
            await ctx.send(i)

    @commands.command(name="spam")
    async def spam(self, ctx, arg, count):
        if ctx.message.guild.id == 812449183415795712:
            await ctx.reply("spam has been blacklisted in sandal server because SOMEONE keeps spamming")
        elif ctx.message.author.id in whitelist:
            if "305299176470872064" in arg:
                await ctx.send("Please dont ping Jag he's so attractive")
            else:
                for i in range(int(count)):
                    await ctx.send(arg)
        else:
            await ctx.reply("You are not whitelisted to use this command!")


def setup(bot: commands.Bot):
    bot.add_cog(Repeat(bot))
