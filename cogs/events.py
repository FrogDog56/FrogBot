import discord
from discord import channel
from discord.abc import User
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client
        client = discord.Client()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} has joined the server")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            colour = discord.Colour.green(),
            title = "Welcome Message",
            description = f"Welcome {member.mention}, enjoy your stay"
      )
        await member.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left the server")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embed = discord.Embed(colour = discord.Colour.green()
        )
        embed.add_field(name="changeprefix:", value="Changes bot command prefix", inline=False)
        embed.add_field(name="pfp (@member):", value="Shows pfp of chosen member", inline=False)
        embed.add_field(name="dog:", value="Sends random picture of a dog", inline=False)
        embed.add_field(name="meme:", value="Sends a random meme into channel", inline=False)
        embed.add_field(name="askdog (Question):", value="Just an 8ball command called askdog", inline=False)
        embed.add_field(name="spamping:", value="Command for trolling/being annoying", inline=False)
        embed.add_field(name="black:", value="Calculates how black u are (it is very accurate)", inline=False)
        embed.add_field(name="kick (@member):", value="Kicks specified member from the server", inline=False)
        embed.add_field(name="tempban (@member) (Number)(Unit):", value="Temporarily bans specified member for a chosen period of time(you can do m for mins, h for hours and d for days)", inline=False)
        embed.add_field(name="ban (@member):", value="Bans specified member until indefinitely", inline=False)
        embed.add_field(name="unban (full user tag):", value="Unbans specified user if already banned", inline=False)
        embed.add_field(name="clear (amount):", value="Clears specified amount messages above the command(by default it will clear five)", inline=False)
        embed.set_footer(text="Bot developed by FrogDog dm FrogDog#0001 if you have any issues")
        
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error: Please input all required arguments")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Error: Command does not exist. Here are my commands")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRole):
            await ctx.send("Error: You do not have the required role to use this command")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Error: You do not have permission to use this command")
            
def setup(client):
    client.add_cog(Events(client))