import discord
import random
from discord.ext import commands
from discord.ext.commands.core import check

class Fun(commands.Cog):

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
    async def odds(self, ctx, range):
        await ctx.send(f"Your odds are {random.randint(1, int(range))}")

    def is_it_frog(ctx):
        return ctx.author.id == 652627153418190881

    @commands.command()
    @commands.check(is_it_frog)
    async def spamping(self, ctx, member, times):
        for x in range(1, int(times)):
            await ctx.send(f"{member}")

             
    @spamping.error
    async def spamping_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.send("Error: You must be FrogDog to use this command")
            
def setup(client):
    client.add_cog(Fun(client))

