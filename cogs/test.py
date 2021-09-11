import discord
import random
from discord import client
from discord.ext import commands
from discord.user import ClientUser

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot logged in as: {ClientUser}")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("hello sir")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"The bots ping is currently unknown")
                 
def setup(client):
    client.add_cog(Test(client))


