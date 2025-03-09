"""Module for the leaderboard command showing language role popularity."""

from __future__ import annotations

from typing import Any

import disnake
from disnake.ext import commands

from dsubot import language_branding
from dsubot.utils.env_handler import bot_config

# Constants for rankings
GOLD = 1
SILVER = 2
BRONZE = 3


class Leaderboard(commands.Cog):
    """A cog for the leaderboard command."""

    def __init__(self, bot: commands.InteractionBot) -> None:
        """Initialize the Leaderboard cog."""
        self.bot = bot

    @commands.slash_command(
        name="leaderboard",
        description="View the popularity leaderboard for programming languages.",
        guild_ids=[bot_config.guild_id],
    )
    async def leaderboard(
        self,
        interaction: disnake.ApplicationCommandInteraction[Any],
    ) -> None:
        """Display a leaderboard showing the member count for each language role."""
        await interaction.response.defer()

        # Get the guild
        guild = interaction.guild
        if not guild:
            return await interaction.followup.send(
                "This command can only be used in a server.",
            )

        # Get all roles matching our language list
        language_roles: list[tuple[disnake.Role, int]] = []

        for role in guild.roles:
            if role.name in language_branding.language_keys:
                # Count members with this role
                member_count = sum(
                    1 for member in guild.members if role in member.roles
                )
                language_roles.append((role, member_count))

        # Sort by member count (highest first)
        language_roles.sort(key=lambda x: x[1], reverse=True)

        # Create the embed
        embed = disnake.Embed(
            title="Language Popularity Leaderboard",
            description="The most popular programming languages in the server:",
            color=disnake.Color.blurple(),
        )

        # Add each language to the embed
        for i, (role, count) in enumerate(language_roles, 1):
            # Get the color info for this language
            color_info = language_branding.language_branding.get(role.name)
            # Use the top language color for the embed (only for first item)
            if i == GOLD and color_info:
                embed.color = color_info.int_value
            # Add emoji based on ranking
            prefix = (
                "🥇"
                if i == GOLD
                else "🥈"
                if i == SILVER
                else "🥉"
                if i == BRONZE
                else f"{i}."
            )
            # Add field with count
            embed.add_field(
                name=f"{prefix} {role.name}",
                value=f"{count} member{'s' if count != 1 else ''}",
                inline=True,
            )

        # If no language roles were found
        if not language_roles:
            embed.description = "No members have chosen a language role yet!"

        # Add footer with total count
        total_members = sum(count for _, count in language_roles)
        embed.set_footer(text=f"Total faction members: {total_members}")

        await interaction.followup.send(embed=embed)
        return None


def setup(bot: commands.InteractionBot) -> None:
    """Set up the Leaderboard cog."""
    bot.add_cog(Leaderboard(bot))
