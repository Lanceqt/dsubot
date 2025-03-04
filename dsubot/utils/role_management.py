"""Provides utility functions for managing roles in a Discord guild.

Functions:
    ensure_language_roles(bot: commands.InteractionBot, guild_id: int) -> None:
        Ensures that all language roles from language_branding exist in the guild.

Constants:
    white_listed_roles (list): A list of roles that are exempt from certain operations.
"""

import logging

import disnake
from disnake.ext import commands

from dsubot import language_branding

logger = logging.getLogger(__name__)
white_listed_roles = ["@everyone", "CTO", "Pedel"]


async def ensure_language_roles(bot: commands.InteractionBot, guild_id: int) -> None:
    """Ensure that all language roles from language_branding exist in the guild.

    Creates any missing roles.
    """
    guild = bot.get_guild(guild_id)
    if not guild:
        logger.error("Guild with ID %s not found.", guild_id)
        return

    all_roles = await guild.fetch_roles()
    existing_roles = {role.name: role for role in all_roles}
    for language, color_info in language_branding.language_branding.items():
        if language in existing_roles:
            logger.info("Role already exists: %s", language)
            continue

        logger.info("Creating role: %s", language)
        try:
            await guild.create_role(
                name=language,
                color=disnake.Color(color_info.int_value),
                reason="Creating language role",
            )
        except disnake.errors.Forbidden:
            logger.exception("Missing permissions to create role: %s", language)
