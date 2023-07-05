from pyot.conf.utils import import_confs
# import pyotred
import discord

from redbot.core import commands, app_commands
from redbot.core import Config
# import_confs("pyotconf")

class RiotCOg(commands.Cog):
    """WALUIGI TIME"""
    def __init__(self, bot):
        self.config = Config.get_conf(self, identifier=1160242069965,force_registration=True)
        self.bot = bot
        default_user = {
            "loluser": "",
            "valorantuser": ""
        }
        self.config.register_user(**default_user)
    
    bind = app_commands.Group(name="bind", description="BOUND")

    @bind.command(name="valorant", description="add Valorant account to user")
    @app_commands.describe(username="Your Player Name")
    async def valorant(self, interaction: discord.Interaction, username: str):
        await self.config.user(interaction.user).valorantuser.set(username)
        userconf = await self.config.user(interaction.user).valorantuser()
        await interaction.response.send_message(f"wowza, info bound\n USER: {interaction.user}\n NAME: {username}\n\n {userconf}")

    @bind.command(name="lol", description="add League of Legends account to user")
    @app_commands.describe(username="Your Summoner Name")
    async def lol(self, interaction: discord.Interaction, username: str):
        await self.config.user(interaction.user).loluser.set(username)
        userconf = await self.config.user(interaction.user).loluser()
        await interaction.response.send_message(f"wowza, info bound\n USER: {interaction.user}\n NAME: {username}\n\n {userconf}")

        
      