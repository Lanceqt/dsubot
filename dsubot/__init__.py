"""Discord bot for the Discord Server Utils (DSU) project.

This package provides functionality for a Discord bot designed to help manage
server utilities, including role management, user interaction, and other
administrative tasks. The bot is built using the disnake library for Discord API
interaction.

Modules:
    utils: Utility functions for bot operations.
    language_branding: Definitions for programming language roles and their styling.

Usage:
    Import the package and access its modules to utilize the bot's functionality.
    Environment variables must be properly configured before running the bot.

Example:
    from dsubot import utils
    utils.role_management.ensure_language_roles(bot, guild_id)

"""

__version__ = "0.1.0"
