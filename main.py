import disnake
import os
from disnake.ext import commands
from dotenv import load_dotenv

from colors import ColorInfo, color_data
import roles

load_dotenv()

# Enable intents (optional, depends on bot needs)
intents = disnake.Intents.default()
intents.members = True  # Needed for member-related events
intents.message_content = True  # Only needed if reading messages
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True
bot = commands.InteractionBot(intents=intents, command_sync_flags=command_sync_flags)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


Languages = commands.option_enum(list(roles.roles.keys()))


@bot.slash_command(
    name="faction",
    description="Pick your side! (this is very important)",
    guild_ids=[1339348789802176623],
)
async def faction(interaction: disnake.ApplicationCommandInteraction, lang: Languages):
    color_name = roles.roles.get(lang)
    if not color_name:
        return await interaction.response.send_message("That language does not exists")
    color_info = color_data.get(color_name)
    await interaction.response.send_message(f"{color_info['hex_code']}")

    print(color_name, color_info)


bot.run(os.getenv("TOKEN"))
