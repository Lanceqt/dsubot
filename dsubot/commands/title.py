"""Module for handling title role assignment for software developers."""

from typing import Any

import disnake
from disnake.ext import commands

from dsubot import title_branding
from dsubot.utils.env_handler import bot_config


class Title(commands.Cog):
    """A cog for handling the title command."""

    def __init__(self, bot: commands.InteractionBot) -> None:
        """Initialize the Title cog."""
        self.bot = bot

    @commands.slash_command(
        name="title",
        description="What is your job title? (example, full-stack developer)",
        guild_ids=[bot_config.guild_id],
    )
    async def title(
        self,
        interaction: disnake.ApplicationCommandInteraction[Any],
        title_choice: str = commands.Param(
            description="The job title you want to set.",
            choices=[
                disnake.OptionChoice(name=title, value=title)
                for title in title_branding.title_branding
            ],
        ),
    ) -> None:
        """Assign a job title to the user by updating their roles."""
        if not interaction.guild:
            await interaction.response.send_message(
                "This command can only be used in a server!",
                ephemeral=True,
            )
            return

        member = interaction.guild.get_member(interaction.user.id)
        if not member:
            await interaction.response.send_message(
                "Could not retrieve member information.",
                ephemeral=True,
            )
            return

        # Find and remove any existing title roles
        existing_title_roles = [
            role for role in member.roles if role.name in title_branding.title_keys
        ]

        for role in existing_title_roles:
            if role.name == title_choice:
                await interaction.response.send_message(
                    f"You already have the title {title_choice}!",
                    ephemeral=True,
                )
                return
            await member.remove_roles(role)

        # Get the role from the guild that matches the chosen title
        new_role = disnake.utils.get(interaction.guild.roles, name=title_choice)
        if not new_role:
            await interaction.response.send_message(
                f"Role for title {title_choice} not found.",
                ephemeral=True,
            )
            return

        await member.add_roles(new_role)
        await interaction.response.send_message(
            f"Your title has been set to {title_choice}.",
            ephemeral=True,
        )
        return


def setup(bot: commands.InteractionBot) -> None:
    """Add the Title cog to the bot."""
    bot.add_cog(Title(bot))
