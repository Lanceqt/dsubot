import os  # noqa: D100

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

import language_branding


def main() -> None:
    """Run the Discord bot."""
    load_dotenv()

    intents = disnake.Intents.default()
    intents = disnake.Intents(members=True, message_content=True)
    command_sync_flags = commands.CommandSyncFlags.default()
    command_sync_flags.sync_commands_debug = True
    bot = commands.InteractionBot(
        intents=intents,
        command_sync_flags=command_sync_flags,
    )

    @bot.slash_command(
        name="faction",
        description="Pick your side! (this is very important)",
        guild_ids=[1339348789802176623],
    )
    async def faction(  # type: ignore  # noqa: PGH003 This is used linter can't see line 23
        interaction: disnake.ApplicationCommandInteraction,  # type: ignore  # noqa: PGH003 can't be resolved from disnake
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

    bot.run(os.getenv("TOKEN"))


if __name__ == "__main__":
    main()
