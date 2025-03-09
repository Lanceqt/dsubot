"""initializes and runs the Discord bot."""

import logging

import disnake
from disnake.ext import commands

from dsubot.utils import role_management
from dsubot.utils.env_handler import bot_config
from dsubot.utils.logging_handler import setup_bot_logging

logger = logging.getLogger(__name__)


def run_bot() -> None:
    """Initialize and runs the Discord bot."""
    setup_bot_logging()

    intents = disnake.Intents(
        members=True,
        message_content=True,
        guilds=True,
        guild_messages=True,
    )
    command_sync_flags = commands.CommandSyncFlags.default()
    command_sync_flags.sync_commands_debug = False
    bot = commands.InteractionBot(
        intents=intents,
        command_sync_flags=command_sync_flags,
    )

    @bot.event
    async def on_ready() -> None:  # type: ignore  # noqa: PGH003
        """Perform housekeeping tasks when the bot is ready."""
        logger.info("Logged in as %s (ID: %s)", bot.user, bot.user.id)
        guild_id = bot_config.guild_id

        await role_management.ensure_language_roles(bot, guild_id)

    bot.load_extension("dsubot.commands.faction")
    bot.load_extension("dsubot.commands.leaderboard")  # Add this line

    bot.run(bot_config.token.get_secret_value())
