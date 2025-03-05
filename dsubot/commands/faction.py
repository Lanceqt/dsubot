"""module implements the faction command."""

from typing import Any

import disnake
from disnake.ext import commands

from dsubot import language_branding
from dsubot.utils.env_handler import bot_config
from dsubot.utils.role_management import white_listed_roles


class Faction(commands.Cog):
    """A cog for handling faction-related commands."""

    def __init__(self, bot: commands.InteractionBot) -> None:
        """Initialize the Faction cog."""
        self.bot = bot

    @commands.slash_command(
        name="faction",
        description="Pick your side! (this is very important)",
        guild_ids=[bot_config.guild_id],
    )
    async def faction(
        self,
        interaction: disnake.ApplicationCommandInteraction[Any],
        lang: str = commands.Param(
            description="The language you want to represent.",
            choices=[
                disnake.OptionChoice(name=language, value=language)
                for language in language_branding.language_branding
            ],
        ),
    ) -> None:
        """Handle the faction command.

        which allows a user to select a lang to represent.
        """
        # Keeping the type checker happy in a best practice but unnecessary way
        if not interaction.guild:
            await interaction.response.send_message(
                "This command can only be used in a server!",
                ephemeral=True,
            )
            return

        member = interaction.guild.get_member(interaction.user.id)
        # Keeping the type checker happy in a best practice but unnecessary way
        if not member:
            await interaction.response.send_message(
                "Could not get member information.",
                ephemeral=True,
            )
            return

        try:
            existing_lang_role = next(
                (
                    role
                    for role in member.roles
                    if role is not None
                    and hasattr(role, "name")
                    and role.name in language_branding.language_keys
                    and role.name not in white_listed_roles
                ),
                None,
            )
            if existing_lang_role:
                if existing_lang_role.name == lang:
                    await interaction.response.send_message(
                        f"You are already representing {lang}!",
                        ephemeral=True,
                    )
                    return
                await member.remove_roles(existing_lang_role)

            new_role = disnake.utils.get(interaction.guild.roles, name=lang)

            if not new_role:
                return

            await member.add_roles(new_role)
            await interaction.response.send_message(
                f"Welcome to the {lang} faction! 🎉",
                ephemeral=True,
            )

        except disnake.Forbidden:
            await interaction.response.send_message(
                "I don't have permission to manage roles!",
                ephemeral=True,
            )
        except disnake.HTTPException as e:
            await interaction.response.send_message(
                f"Failed to manage roles: {e!s}",
                ephemeral=True,
            )


async def remove_existing_roles(
    role_to_add: str,
    member: disnake.Member,
    interaction: disnake.ApplicationCommandInteraction[Any],  # I cringe at this
) -> None:
    """Remove any existing roles that are not the one to be added, and if the user is
    already representing the faction, send a message.

    Remove any existing roles that are not the one to be added, and if the user is
    already representing the faction, send a message.

    """  # noqa: D205
    existing_lang_roles = [
        role
        for role in member.roles
        if role is not None
        and hasattr(role, "name")
        and role.name in language_branding.language_keys
        and role.name not in white_listed_roles
    ]

    for existing in existing_lang_roles:
        if existing.name != role_to_add:
            await member.remove_roles(existing)
        else:
            return await interaction.response.send_message(
                f"You are already representing {role_to_add}!",
                ephemeral=True,
            )
    return None


def setup(bot: commands.InteractionBot) -> None:
    """Add the Faction cog to the bot."""
    bot.add_cog(Faction(bot))
