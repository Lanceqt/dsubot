# src/dsubot/commands/faction.py
"""module implements the faction command."""

import disnake
from disnake.ext import commands

from dsubot import language_branding


class Faction(commands.Cog):
    """A cog for handling faction-related commands."""

    def __init__(self, bot: commands.InteractionBot) -> None:
        """Initialize the Faction cog."""
        self.bot = bot

    @commands.slash_command(
        name="faction",
        description="Pick your side! (this is very important)",
        guild_ids=[1339348789802176623],
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
        color_info = language_branding.language_branding.get(lang)

        if color_info:
            color_int = color_info.int_value
            guild = interaction.guild
            member = interaction.author

            if not guild:
                await interaction.response.send_message(
                    "This command must be used in a server.",
                    ephemeral=True,
                )
                return

            if not isinstance(member, disnake.Member):
                await interaction.response.send_message(
                    "This command must be used by a member.",
                    ephemeral=True,
                )
                return

            current_faction_roles: list[disnake.Role] = [
                role
                for role in member.roles
                if role is not None
                and role.name.endswith(" Faction")
                and role.name.replace(" Faction", "")
                in language_branding.language_branding
            ]

            role_name: str = f"{lang} Faction"
            new_role = disnake.utils.get(guild.roles, name=role_name)

            if not new_role:
                new_role = await guild.create_role(
                    name=role_name,
                    color=disnake.Color(color_int),
                    reason="User chose a faction.",
                )

            changing_faction = bool(current_faction_roles)
            old_role_name: str | None = None
            if changing_faction:
                old_role_name = current_faction_roles[0].name
                await member.remove_roles(
                    *current_faction_roles,
                    reason="User changed faction.",
                )
                message = f"you have changed your faction from {old_role_name} to {role_name}."
            else:
                message = f"You chose {lang} Faction!"
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
            if not new_role:
                # Role creation failed
                await interaction.response.send_message(
                    "I couldn't create the faction role. Please check bot permissions.",
                    ephemeral=True,
                )
                await member.add_roles(new_role, reason="Assigning new faction")
        else:
            await interaction.response.send_message(
                f"Sorry, the language '{lang}' is not supported.",
                ephemeral=True,
            )


def setup(bot: commands.InteractionBot) -> None:
    """Add the Faction cog to the bot."""
    bot.add_cog(Faction(bot))
