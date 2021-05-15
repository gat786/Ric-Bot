"""
This module controls the Discord client behavior.

Classes: Discord
Functions: runClient()
"""
from modules.settings import loadSettings, runDiscordBot
from discord.ext import commands


class Discord(commands.Bot):
    """
    Discord bot client class.

    Methods:
        on_ready(self)
        loadCogs(self)
    """

    def __init__(self, command_prefix, help_command=None):
        super().__init__(command_prefix=command_prefix, help_command=help_command)
        self.loadCogs()

    async def on_ready(self):
        """Displays success message if connection is successful."""
        print("Logged on as", self.user)

    def loadCogs(self):
        """Loads the cogs that handles individual commands"""
        # Hard code can be avoided, I'll move the cogs files into a folder named cogs
        # And use os.listdir() to load the modules
        cogs = ['help', 'memes', 'quotes', 'antispam', 'ping', 'offensive']
        for cog in cogs:
            self.load_extension(f'modules.{cog}')


def runClient():
    """This method loads the environment variables and runs the Discord bot client."""
    loadSettings()
    client = Discord(command_prefix="!", help_command=None)
    runDiscordBot(client)
