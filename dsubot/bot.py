"""initializes and runs the Discord bot."""

import logging
import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

from dsubot.utils import role_management  # Import the new module


def setup_logging() -> None:
    """Configure logging for the bot."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


logger = logging.getLogger(__name__)


def run_bot() -> None:
    """Initialize and runs the Discord bot."""
    setup_logging()
    load_dotenv()

    intents = disnake.Intents(members=True, message_content=True, guilds=True)
    command_sync_flags = commands.CommandSyncFlags.default()
    command_sync_flags.sync_commands_debug = True
    bot = commands.InteractionBot(
        intents=intents,
        command_sync_flags=command_sync_flags,
    )

    @bot.event
    async def on_ready() -> None:  # type: ignore  # noqa: PGH003
        """Perform housekeeping tasks when the bot is ready."""
        logger.info("Logged in as %s (ID: %s)", bot.user, bot.user.id)
        guild_id = 1339348789802176623  # Replace with your actual guild ID

        await role_management.ensure_language_roles(bot, guild_id)

    bot.load_extension("dsubot.commands.faction")

    bot.run(os.getenv("TOKEN"))
