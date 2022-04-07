from os import name
import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(colour = discord.Colour.green(),
                              title = "Here are my commands"
        
        )
        embed.add_field(name="changeprefix:", value="Changes bot command prefix", inline=False)
        embed.add_field(name="pfp (@member):", value="Shows pfp of chosen member", inline=False)
        embed.add_field(name="dog:", value="Sends random picture of a dog", inline=False)
        embed.add_field(name="meme:", value="Sends a random meme into channel", inline=False)
        embed.add_field(name="askdog (Question):", value="Just an 8ball command called askdog", inline=False)
        embed.add_field(name="spamping (user) (times):", value="Command for trolling/being annoying", inline=False)
        embed.add_field(name="odds (range):", value="Returns a random number", inline=False)
        embed.add_field(name="kick (@member):", value="Kicks specified member from the server", inline=False)
        embed.add_field(name="tempban (@member) (Number)(Unit):", value="Temporarily bans specified member for a chosen period of time(you can do m for mins, h for hours and d for days)", inline=False)
        embed.add_field(name="ban (@member):", value="Bans specified member until indefinitely", inline=False)
        embed.add_field(name="unban (full user tag):", value="Unbans specified user if already banned", inline=False)
        embed.add_field(name="clear (amount):", value="Clears specified amount messages above the command(by default it will clear five)", inline=False)
        embed.set_footer(text="Bot developed by FrogDog dm FrogDog#0001 if you have any issues")
        
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))