# src/dsubot/commands/faction.py
"""module implements the faction command."""

import os

import disnake
from disnake.ext import commands

from dsubot import language_branding

guild_id = os.getenv("GUILD_ID")

if guild_id is None:
    error = "guild_id is not set in the environment variables."
    raise ValueError(error)

guild_id = int(guild_id)


class Faction(commands.Cog):
    """A cog for handling faction-related commands."""

    def __init__(self, bot: commands.InteractionBot) -> None:
        """Initialize the Faction cog."""
        self.bot = bot

    @commands.slash_command(
        name="faction",
        description="Pick your side! (this is very important)",
        guild_ids=[guild_id],
    )
    async def faction(
        self,
        interaction: disnake.ApplicationCommandInteraction,  # type: ignore  # noqa: PGH003
        lang: str = commands.Param(
            description="The language you want to represent.",
            choices=[
                disnake.OptionChoice(name=language, value=language)
                for language in language_branding.language_branding
            ],
        ),
    ) -> None:
        """Assign a faction role to a user based on their language choice."""
        # This part below is probably not needed except for best practices
        # Disnake handles this via slash commands to the best of my knowledge.
        color_info = language_branding.language_branding.get(lang)
        if not color_info:
            await interaction.response.send_message(
                f"Sorry, the language '{lang}' is not supported.",
                ephemeral=True,
            )
            return

        # Also not entirely sure we need this part below
        color_int = color_info.int_value
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message(
                "This command must be used in a server.",
                ephemeral=True,
            )
            return
        # This part below is probably not needed except for best practices
        member = interaction.author
        if not isinstance(member, disnake.Member):
            await interaction.response.send_message(
                "This command must be used by a member.",
                ephemeral=True,
            )
            return

        print(
            f"DEBUG: Member {member.display_name} has roles: {[role.name for role in member.roles if role is not None]}"
        )
        print(
            f"DEBUG: Available language roles: {list(language_branding.language_branding.keys())}"
        )

        current_faction_roles: list[disnake.Role] = [
            role
            for role in member.roles
            if role is not None
            and role.name in list(language_branding.language_branding.keys())
        ]

        print(
            f"DEBUG: Detected faction roles: {[role.name for role in current_faction_roles if role is not None]}"
        )
        role_name: str = lang
        new_role = disnake.utils.get(guild.roles, name=role_name)

        if not new_role:
            try:
                new_role = await guild.create_role(
                    name=role_name,
                    color=disnake.Color(color_int),
                    reason="User chose a faction.",
                )
            except disnake.errors.Forbidden:
                await interaction.response.send_message(
                    "I couldn't create the faction role. Please check bot permissions.",
                    ephemeral=True,
                )
                return

        # I don't think I need this
        if not new_role:
            await interaction.response.send_message(
                "Failed to create or find the faction role.",
                ephemeral=True,
            )
            return
        message: str = ""
        if current_faction_roles:
            old_role_name = current_faction_roles[0].name
            await member.remove_roles(
                *current_faction_roles,
                reason="User changed faction.",
            )
            message = (
                f"you have changed your faction from {old_role_name} to {role_name}."
            )
        else:
            message = f"You chose {lang}"
        await member.add_roles(new_role, reason="Assigning new faction")
        print(
            f"DEBUG: After adding new role, roles: {[role.name for role in member.roles if role is not None]}"
        )
        try:
            await interaction.author.send(message)
            await interaction.response.send_message(
                "I've sent you a DM with your faction information!",
                ephemeral=True,
            )
        except disnake.errors.Forbidden:
            await interaction.response.send_message(
                "I couldn't send you a DM. Please make sure your DMs are open.",
                ephemeral=True,
            )


def setup(bot: commands.InteractionBot) -> None:
    """Add the Faction cog to the bot."""
    bot.add_cog(Faction(bot))
