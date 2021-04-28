from discord.ext import commands
"""
This module implements the ping command for the bot.

Classes: Ping
Functions: 
    setup(client)
"""


class Ping(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        """Handles ping command"""
        await ctx.send(f"pong {round(self.client.latency) * 1000}ms")


def setup(client):
    client.add_cog(Ping(client))
