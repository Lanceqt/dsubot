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

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotConfig(BaseSettings):
    """Configuration class for the bot settings.

    Attributes:
        model_config (SettingsConfigDict): Configuration for the settings model,
        specifying the environment file.
        guild_id (int): The ID of the guild (server) the bot is associated with.
        token (SecretStr): The secret token used for authenticating the bot.

    """

    model_config = SettingsConfigDict(env_file=".env")
    guild_id: int
    token: SecretStr


# type ignore: This is an annoying workaround for the fact that pydantic will
# automatically fill in the missing values from the .env
# but it doesn't "know" that, so it thinks
#  we have to provide both guild_id and token to `BotConfig`
bot_config = BotConfig()  # type: ignore - see above
