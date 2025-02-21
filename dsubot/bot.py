"""initializes and runs the Discord bot."""

import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

from dsubot.utils import role_management  # Import the new module


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

    @bot.event
    async def on_ready() -> None:  # type: ignore  # noqa: PGH003
        """Perform housekeeping tasks when the bot is ready."""
        print(f"Logged in as {bot.user} (ID: {bot.user.id})")
        guild_id = 1339348789802176623  # Replace with your actual guild ID

        await role_management.ensure_language_roles(bot, guild_id)  # Call the funct

    # Load commands from the commands directory
    bot.load_extension("dsubot.commands.faction")

    bot.run(os.getenv("TOKEN"))
