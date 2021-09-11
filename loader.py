import discord
import os
import json
from discord import activity
from discord.ext import commands, tasks
from itertools import cycle

def get_prefix(client, message):
    with open("bot.main\prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix= get_prefix, intents=intents, help_command=None)
stat = cycle(["(prefix)help to view commands",". is my default prefix"])

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

for filename in os.listdir("./bot.main/cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.do_not_disturb)
    print("Status updated", "\nRPC established", "\nLoop initialized")

@tasks.loop(seconds=7)
async def change_status():
    await client.change_presence(activity=discord.Game(next(stat)))

@client.event
async def on_guild_join(guild):
    with open("bot.main\prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "."

    with open("bot.main\prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=2)

@client.event
async def on_guild_remove(guild):
    with open("bot.main\prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("bot.main\prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=2)

@client.command()
async def changeprefix(ctx, prefix):
    with open("bot.main\prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("bot.main\prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=2)

    await ctx.send(f"Prefix was successfully changed to: {prefix}")

@client.event
async def on_member_join(member):
    #input server id
    guild = client.get_guild(000000000000000)
    #input channel id
    channel = guild.get_channel(00000000000000)
    await channel.send(f"Welcome to the server {member.mention}")

@client.event
async def on_member_remove(member):
    #input server id
    guild = client.get_guild(000000000000000)
    #input channel id
    channel = guild.get_channel(0000000000000000)
    await channel.send(f"{member.mention} has left the server")


client.run("inset bot token")