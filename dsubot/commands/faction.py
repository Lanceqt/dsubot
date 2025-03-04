"""module implements the faction command."""

import disnake
from disnake.ext import commands

from dsubot import language_branding
from dsubot.utils.env_handler import GUILD_ID
from dsubot.utils.role_management import white_listed_roles


class Faction(commands.Cog):
    """A cog for handling faction-related commands."""

    def __init__(self, bot: commands.InteractionBot) -> None:
        """Initialize the Faction cog."""
        self.bot = bot

    @commands.slash_command(
        name="faction",
        description="Pick your side! (this is very important)",
        guild_ids=[GUILD_ID],
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
            if existing_lang_role is not None:
                if existing_lang_role.name == lang:
                    await interaction.response.send_message(
                        f"You are already representing {lang}!",
                        ephemeral=True,
                    )
                    return
                await member.remove_roles(existing_lang_role)
                return

            new_role = disnake.utils.get(interaction.guild.roles, name=lang)
            if new_role:
                await member.add_roles(new_role)
                await interaction.response.send_message(
                    f"Welcome to the {lang} faction! 🎉",
                    ephemeral=True,
                )
                return

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


def setup(bot: commands.InteractionBot) -> None:
    """Add the Faction cog to the bot."""
    bot.add_cog(Faction(bot))
