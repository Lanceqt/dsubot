"""Provides utilities for handling environment variables required by the bot.

This module encapsulates the retrieval and validation of environment variables
that are essential for the bot's operation. It ensures that required values
are present and correctly formatted.

Functions:
    get_guild_id(): Retrieves the Discord guild ID from environment variables.
    get_bot_token(): Retrieves the bot token from environment variables.

Constants:
    GUILD_ID: The Discord guild ID for the bot to operate in.
    BOT_TOKEN: The Discord bot token for authentication.

Raises:
    ValueError: If a required environment variable is not set.

"""

import os


def get_guild_id() -> int:
    """Get the guild ID from environment variables."""
    guild_id = os.getenv("GUILD_ID")
    if guild_id is None:
        error = "guild_id is not set in the environment variables."
        raise ValueError(error)
    return int(guild_id)


def get_bot_token() -> str:
    """Get the bot token from environment variables."""
    token = os.getenv("TOKEN")
    if token is None:
        error = "TOKEN is not set in the environment variables."
        raise ValueError(error)
    return token


GUILD_ID = get_guild_id()
BOT_TOKEN = get_bot_token()
