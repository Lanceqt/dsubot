import disnake
from disnake.ext import commands

from dsubot import language_branding


async def ensure_language_roles(bot: commands.InteractionBot, guild_id: int) -> None:
    """Ensure that all language roles from language_branding exist in the guild.

    Creates any missing roles.
    """
    guild = bot.get_guild(guild_id)
    if not guild:
        print(f"Guild with ID {guild_id} not found.")
        return

    existing_roles = {role.name: role for role in guild.roles}

    for language, color_info in language_branding.language_branding.items():
        if language not in existing_roles:
            print(f"Creating role: {language}")
            try:
                await guild.create_role(
                    name=language,
                    color=disnake.Color(color_info.int_value),
                    reason="Creating language role",
                )
            except disnake.errors.Forbidden:
                print(f"Missing permissions to create role: {language}")
        else:
            print(f"Role already exists: {language}")
