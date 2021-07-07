import discord
from discord.ext import commands
#from dislash import *
from util.secret_config import token

bot = commands.Bot(
    command_prefix="o ",
    allowed_mentions=discord.AllowedMentions(
        users=True,         # Whether to ping individual user @mentions
        everyone=True,      # Whether to ping @everyone or @here mentions
        roles=True,         # Whether to ping role @mentions
        replied_user=False,  # Whether to ping on replies to messages
    ),
)

#slash = SlashClient(bot)
#guilds = [802883640286773269]


@bot.event
async def on_ready():
    print("Obie trice, real name no gimmicks")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="amamamamamamama"))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.reply("Only my owner can use this command!")

bot.load_extension("jishaku")
bot.load_extension("repeat")
bot.load_extension("trolling")
bot.load_extension("rand")
bot.load_extension("owo")
bot.load_extension("rater")
bot.load_extension("embed")
bot.load_extension("skyblock")

bot.run(token)
