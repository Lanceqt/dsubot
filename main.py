import os  # noqa: D100

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

import language_branding

load_dotenv()

intents = disnake.Intents.default()
intents = disnake.Intents(members=True, message_content=True)
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True
bot = commands.InteractionBot(intents=intents, command_sync_flags=command_sync_flags)


@bot.slash_command(
    name="faction",
    description="Pick your side! (this is very important)",
    guild_ids=[1339348789802176623],
)
async def faction(
    interaction: disnake.ApplicationCommandInteraction,  # type: ignore  # noqa: PGH003
    lang: str = commands.Param(
        description="The language you want to represent.",
        choices=[
            disnake.OptionChoice(name=lang, value=lang)
            for lang in language_branding.language_keys
        ],
    ),
) -> None:
    """Assign a faction role to a user based on their language choice."""
    color_int: int = language_branding.language_branding[lang]["int_value"]
    await interaction.response.send_message(
        f"You chose {lang} with color {color_int}!",
    )


bot.run(os.getenv("TOKEN"))
