import discord
from discord.ext import commands
#from dislash import *
from dotenv import load_dotenv
from os import getenv
load_dotenv()
token = getenv("TOKEN")

bot = commands.Bot(command_prefix="o ")
#slash = SlashClient(bot)
#guilds = [802883640286773269]


@bot.event
async def on_ready():
    print("Obie trice, real name no gimmicks")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="amamamamamamama"))


bot.load_extension("repeat")
bot.load_extension("trolling")
bot.load_extension("rps")
bot.load_extension("owo")
bot.load_extension("rater")
bot.load_extension("embed")

bot.run(token)
