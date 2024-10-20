from __future__ import annotations

from logging import getLogger
from typing import Optional

from discord.ext import commands

from src.cogs import EXTENTIONS

log= getLogger(__name__)
import discord

__all__ = (
    "Bot",
)

class Bot(discord.ext.commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
        )
    async def on_ready(self) -> None:
        log.info(f"logged in as {self.user}")
    
    async def success(self, content: str, interaction: discord.Interaction, ephemeral: Optional[bool]):
        """Sending success Message"""
        pass
    async def   error(self, content: str, interaction: discord.Interaction, ephemeral: Optional[bool]):
        """Sending error Message"""
        pass

    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type == discord.InteractionType.application_command:
            log.info(f"[INTERACTION] [{interaction.id}] Received Interaction:")
            log.info(f"[INTERACTION] [{interaction.id}] > Guild: {interaction.guild or 'None'}")
            log.info(f"[INTERACTION] [{interaction.id}] > Channel: {interaction.channel or 'None'}")
            log.info(f"[INTERACTION] [{interaction.id}] > User: {interaction.user or 'None'}")

            log.info(f"[INTERACTION] [{interaction.id}] > Command: {interaction.data['name'] or 'None'}")
            log.info(f"[INTERACTION] [{interaction.id}] > > Options: {interaction.data.get('options', [])}")

    async def setup_hook(self):
        log.info(f"Loading {len(EXTENTIONS)} extensions")
        for extension in EXTENTIONS:
            log.info(f"Loading {extension}")
            await self.load_extension(extension)
        log.info("All extentions loaded")