import discord
import random
from discord import embeds
from discord.embeds import Embed
from discord.ext import commands

class GeneralCmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pfp(self, ctx, member: discord.Member):
        embed = discord.Embed(colour = discord.Colour.green(),
                              title = member.name,
                              description = member.mention
        )
        embed.add_field(name = "ID:", value = member.id, inline = True)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(text = "Bot developed by FrogDog dm FrogDog#0001 if you have any issues")
        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        embed = discord.Embed(colour = discord.Colour.green(),
                              title = "Doggo!")
        dogs = ["https://cdn.discordapp.com/attachments/863814612041203725/877962273363230790/R8se5g1b.jpg",
                "https://cdn.discordapp.com/attachments/863814612041203725/877994583064207401/1SSVsBHb.jpg",
                "https://cdn.discordapp.com/attachments/863814612041203725/877994932445511690/JXetxQhb.jpg",
                "https://cdn.discordapp.com/attachments/863814612041203725/877995153229484042/lZA8Kx7b.jpg",
                "https://cdn.discordapp.com/attachments/863814612041203725/878010360525889587/8pTwPlXb.jpg",
                "https://cdn.discordapp.com/attachments/863814612041203725/878010564020957234/zfmhZ27b.gif",
                "https://cdn.discordapp.com/attachments/863814612041203725/878010591028084776/aJYZ20vb.jpg",
                "https://cdn.discordapp.com/attachments/863814612041203725/878010671235731466/fSgnUKWb.jpg"
                
        
        ]
        
        random_link = random.choice(dogs)

        embed.set_image(url = random_link)
        embed.set_footer(text= "Bot developed by FrogDog dm FrogDog#0001 if you have any issues")

        await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):
        embed = discord.Embed(colour = discord.Colour.green(),
                              title = "Meme!")
        memes = ["https://cdn.discordapp.com/attachments/873352507475263578/875813151495585852/cat_has_the_raygun1-1.jpg",
                 "https://cdn.discordapp.com/attachments/821023610781040651/855805640224145408/image0.png",
                 "https://cdn.discordapp.com/attachments/821023610781040651/856012569437011998/image0.png",
                 "https://cdn.discordapp.com/attachments/821023610781040651/843306852216471592/IMG-20201014-WA0000.jpg",
                 "https://cdn.discordapp.com/attachments/821023610781040651/843306671185985576/Big-brain-move.jpg",
                 "https://cdn.discordapp.com/attachments/821023610781040651/843306660202283068/20201210_234544.png",
                 "https://cdn.discordapp.com/attachments/821023610781040651/827934887637024768/Screenshot_20210403_161210.jpg",
                 
        ]
        
        random_link = random.choice(memes)

        embed.set_image(url = random_link)
        embed.set_footer(text= "Bot developed by FrogDog dm FrogDog#0001 if you have any issues")

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(GeneralCmds(client))
