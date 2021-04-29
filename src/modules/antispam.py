"""
This module implements the antispam feature for the bot.

Classes: AntiSpam
Functions: 
    has_links(message)
    setup(client)
"""

from re import search
from discord.ext import commands


class AntiSpam(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if has_links(message):
            await message.delete()
            await message.channel.send(
                "Links not allowed in this channel", delete_after=15
            )


def setup(client):
    client.add_cog(AntiSpam(client))


links_not_allowed = (
    829038892145311775,
    829039782260244561,
)  # moderator only and welcome channel
allowed_url = "https://github.com/"


def has_links(message) -> bool:
    """
    Checks if message that contains links was posted in an allowed channel.

    Args: message from Discord chat

    Returns: True or False, depending on channel check.
    """
    url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'#\".,<>?«»“”‘’]))"
    if (
        search(url_regex, message.content)
        and message.channel.id in links_not_allowed
        and not message.content.startswith(allowed_url)
    ):
        return True
    return False
