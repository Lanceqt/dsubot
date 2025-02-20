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
            try:
                await interaction.author.send(
                    f"You chose {lang} with color {color_int}!",
                )
                await interaction.response.send_message(
                    "I've sent you a DM with your faction information!",
                    ephemeral=True,
                )
            except disnake.errors.Forbidden:
                await interaction.response.send_message(
                    "I couldn't send you a DM. Please make sure your DMs are open.",
                    ephemeral=True,
                )
        else:
            await interaction.response.send_message(
                f"Sorry, the language '{lang}' is not supported.",
                ephemeral=True,
            )


def setup(bot: commands.InteractionBot) -> None:
    """Add the Faction cog to the bot."""
    bot.add_cog(Faction(bot))
