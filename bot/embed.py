import discord, random
from discord.ext import commands

class owo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="reps")
    async def test(self, ctx):
        embed=discord.Embed(title=" ", color=0x605ac6)
        embed.set_author(name=f"Reputation Summary - {ctx.author.name}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Today", value=random.randint(0, 2147483647), inline=True)
        embed.add_field(name="Last 7 Days", value=random.randint(0, 2147483647), inline=True)
        embed.add_field(name="All Time", value=random.randint(0, 2147483647), inline=True)
        embed.add_field(name="Crafts", value=random.randint(0, 2147483647), inline=True)
        embed.add_field(name="Transfers", value=random.randint(0, 2147483647), inline=True)
        embed.add_field(name="Middlemans", value=random.randint(0, 2147483647), inline=True)
        embed.add_field(name="High Value Rep", value=random.randint(0, 2147483647), inline=True)
        embed.add_field(name="Event / Special", value=random.randint(0, 2147483647), inline=True)
        embed.add_field(name="Unique Repper %", value=str(random.randint(1, 100)) + "%", inline=True)
        embed.set_footer(text="Note: Review rep using /rep list before deciding to trust someone & read channel pins for more information on staying safe.")
        await ctx.send(embed=embed)
 

def setup(bot: commands.Bot):
    bot.add_cog(owo(bot))
