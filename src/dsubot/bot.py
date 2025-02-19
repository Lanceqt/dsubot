# src/dsubot/bot.py
"""initializes and runs the Discord bot."""

import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv


def run_bot() -> None:
    """Initialize and runs the Discord bot."""
    load_dotenv()

    intents = disnake.Intents.default()
    intents = disnake.Intents(members=True, message_content=True)
    command_sync_flags = commands.CommandSyncFlags.default()
    command_sync_flags.sync_commands_debug = True
    bot = commands.InteractionBot(
        intents=intents,
        command_sync_flags=command_sync_flags,
    )

    # Load commands from the commands directory
    bot.load_extension("dsubot.commands.faction")

    bot.run(os.getenv("TOKEN"))
