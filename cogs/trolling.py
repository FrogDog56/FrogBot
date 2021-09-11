import discord
import random
from discord.ext import commands
from discord.ext.commands.core import check

class Funny(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def askdog(self, ctx, *, question):
        responses = ["It is certain.",
                        "It is decidedly so.",
                        "Without a doubt.",
                        "Yes, definitely.",
                        "You may rely on it.",
                        "As I see it, yes.",
                        "Most likely.",
                        "Outlook good."
        ]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


    @commands.command()
    async def black(self, ctx):
            responses = ["90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%", "10%", "0%"]
            await ctx.send(f"You are {random.choice(responses)} black")

    def is_it_frog(ctx):
        return ctx.author.id == 652627153418190881

    @commands.command()
    @commands.check(is_it_frog)
    async def spamping(self, ctx, member):
            await ctx.send(f"@{member}")
            await ctx.send(f"@{member}")
            await ctx.send(f"@{member}")
            await ctx.send(f"@{member}")
            await ctx.send(f"@{member}")
            await ctx.send(f"@{member}")
            await ctx.send(f"@{member}")
            await ctx.send(f"@{member}")
             
    @spamping.error
    async def spamping_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.send("Error: You must be FrogDog to use this command")
            
def setup(client):
    client.add_cog(Funny(client))

