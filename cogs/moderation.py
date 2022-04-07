import discord
import asyncio
from discord.ext import commands
from discord.ext.commands.core import command

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason = reason)
        await ctx.send(f"{member} has been booted")

    class DurationConverter(commands.Converter):
        async def convert(self, ctx, argument):
            amount = argument[:-1]
            unit = argument[-1]

            if amount.isdigit() and unit in ["m", "h", "d"]:
                return (int(amount), unit)

            raise commands.BadArgument(message = "Not a valid amount of time")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def tempban(self, ctx, member: commands.MemberConverter, duration: DurationConverter):

        multiplier = {"m": 60, "h" : 3600, "d": 86400}
        amount, unit = duration

        await ctx.guild.ban(member)
        await ctx.send(f"{member} has been banned for {amount}{unit}")
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
          await ctx.send("Error: Please input full discord tag for command to work")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Moderation(client))
