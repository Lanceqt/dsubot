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

bot = commands.InteractionBot(intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


Languages = commands.option_enum(list(roles.roles.keys()))


@bot.slash_command(name="foo", description="Says bar!")
async def faction(interaction: disnake.ApplicationCommandInteraction, lang: Languages):
    color_info = color_data.get(lang)
    if color_info:
        await interaction.response.send_message(f"{color_info['hex_code']}")
    else:
        await interaction.response.send_message("That language does not exists")


bot.run(os.getenv("TOKEN"))
