import os  # noqa: D100
from typing import Literal

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

import roles
from colors import color_data

load_dotenv()

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True
bot = commands.InteractionBot(intents=intents, command_sync_flags=command_sync_flags)

LanguageKeys = Literal[tuple(roles.roles.keys())]


@bot.slash_command(
    name="faction",
    description="Pick your side! (this is very important)",
    guild_ids=[1339348789802176623],
)
async def faction(  # noqa: D103
    interaction: disnake.ApplicationCommandInteraction,  # type: ignore  # noqa: PGH003
    lang: str,
) -> None:


"""     color_name = roles.roles.get(lang)
    if not color_name:
        await interaction.response.send_message("That language does not exists")
        return

    color_info = color_data.get(color_name)
    if color_info is None:
        await interaction.response.send_message(
            "Color information not found for that language.",
        )
        return

    hex_code = color_info.get("hex_code")  # Use .get() to handle missing keys

    if hex_code is None:
        await interaction.response.send_message("Hex code not found for that language.")
        return

    await interaction.response.send_message(f"{color_info['hex_code']}") """


bot.run(os.getenv("TOKEN"))
