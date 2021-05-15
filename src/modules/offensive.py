"""
This module implements the offensive words feature for the bot.

Classes: Offensive
Functions:
    is_offensive(message)
    setup(client)
"""

import discord
from discord.ext import commands
from os import path
import json

PATH = path.join("src", 'modules', "")  # Space to add appropriate slash (/,\)


class Offensive(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if is_offensive(message.content):
            await message.reply(
                f"{message.author.mention} Offensive language is not allowed!!"
            )
            try:
                await message.delete()
            except discord.errors.Forbidden as e:
                await message.reply(
                    "`Abusive content found but not enough permissions available to delete the message.`\n" +
                    "`Try inviting the bot with administrator permission.`"
                )


def setup(client):
    client.add_cog(Offensive(client))


def is_offensive(message):
    """
    Checks if message that contains offensive words.

    Args: message from Discord chat

    Returns: True or False, depending on offensive word found or not.
    """

    JSON_OBJ = {}

    with open(PATH + "offensive.json", 'r') as f:
        JSON_OBJ = json.load(f)

    message = message.split()

    for word in message:
        if JSON_OBJ.get(word.lower()):
            return True
    return False

    """
    I had one more implementation that goes like this
    

    message = message.lower()
    for word in JSON_OBJ:
        if word.lower() in message:
            return True
    return False

    The only problem with this is that it flags words like Dickens, Douglass, buttler
    """
