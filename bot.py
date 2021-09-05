import discord
from discord.ext import commands
from discord.ext.commands import bot_has_permissions, Bot, BotMissingPermissions, guild_only
from discord import Member
from secret import token
import os
import asyncio
import random

#Prefix can be changed here
prefix = ";"

intents = discord.Intents.default()
intents = discord.Intents(messages = True, guilds = True)


bot = commands.Bot(command_prefix = prefix, intents = intents)
bot.remove_command("help")

#Prints output to terminal if all is well
@bot.event
async def on_ready():
    print("We're clear for takeoff!")
    await bot.change_presence(activity = discord.Game("Going Insane | ;help"))

#Rough draft, I'll make this better soon
#@client.event
#async def on_command_error(ctx, error, message):
    #if isinstance(error, discord.ext.commands.CommandNotFound):
        #await ctx.send("Command at {0} is not recognized.".format(message))

#Secret command wo
@bot.command()
async def sleep(ctx):
    owner_id = "687081333876719740"
    if str(ctx.message.author.id) == str(owner_id):
        await ctx.send("Goodnight...")
        print("User terminated the bot.")
        quit()
    else:
        await ctx.send("Only the bot owner can use this command!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension("cogs.{0}".format(filename[:-3]))
        
print("Second stage clear")
bot.run(token)
