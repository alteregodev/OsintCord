import disnake
import datetime
import aiofiles
from disnake.ext import commands

from utils.utils import *

def load(bot: commands.Bot):
    @bot.event
    async def on_ready():
        current_time = datetime.datetime.now()

        print(f'\nLogged in as {bot.user}')
        print(f'Current time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}')

    @bot.slash_command(description='Check bot\'s latency')
    async def ping(inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(
            title='Pong!',
            description=f'Bot\'s latency - `{round(bot.latency * 1000, 2)}ms`'
        )
        await inter.response.send_message(embed=embed)

    @bot.slash_command(description='Get information about a user')
    async def user_info(inter: disnake.ApplicationCommandInteraction, user_id):
        try:
            user_id = int(user_id.strip()) # No, you can't just "id: int", because discord doesn't allow to pass big numbers as an argument for some reason
        except TypeError:
            error_embed = await get_error_embed('Please enter a valid id')
            await inter.response.send_message(embed=error_embed, ephemeral=True)

        try:
            user = await bot.fetch_user(user_id)
            embed = disnake.Embed(
                title=f'Information about {user.name}',
                description=f'''
                    > User ID : `{user.id}`
                    > User display name : `{user.display_name}`
                    > Is a bot : `{user.bot}`
                    > Profile accent color : `{user.accent_color}`
                    > User account created at : `{user.created_at.strftime('%Y-%m-%d %H:%M:%S')}`
                '''
            )
            if user.avatar:
                embed.set_thumbnail(url=user.avatar.url)

            if user.banner:
                embed.set_image(url=user.banner)

            await inter.response.send_message(embed=embed)

        except disnake.NotFound:
            error_embed = await get_error_embed('Didn\'t find a user with such id')
            await inter.response.send_message(embed=error_embed, ephemeral=True)

    @bot.slash_command(description='Get information about a guild')
    async def guild_info(inter: disnake.ApplicationCommandInteraction, guild_id):
        try:
            guild_id = int(guild_id.strip()) # No, you can't just "id: int", because discord doesn't allow to pass big numbers as an argument for some reason
        except TypeError:
            error_embed = await get_error_embed('Please enter a valid id')
            await inter.response.send_message(embed=error_embed, ephemeral=True)

        try:
            guild = await bot.fetch_guild(guild_id)
            embed = disnake.Embed(
                title=f'Information about {guild.name}',
                description=f'''
                    > Guild ID : `{guild.id}`
                    > Guild created at : `{guild.created_at.strftime('%Y-%m-%d %H:%M:%S')}`
                '''
            )
            if guild.icon:
                embed.set_thumbnail(url=guild.icon.url)

            if guild.banner:
                embed.set_image(url=guild.banner.url)

            await inter.response.send_message(embed=embed)

        except disnake.NotFound:
            error_embed = await get_error_embed('Didn\'t find a guild with such id (usually this means I am not in this guild)')
            await inter.response.send_message(embed=error_embed, ephemeral=True)

    @bot.slash_command(description='Get information about the bot')
    async def about(inter: disnake.ApplicationCommandInteraction):
        version = await get_file_content('.version')
        embed = disnake.Embed(
            title=f'OsintCord {version}',
            description='''
                > Developer - [GitHub](https://github.com/alteregodev)
                > Made with - `Python, Disnake, Love <3`
                > Bot\'s GitHub - [GitHub Repo](https://github.com/alteregodev/OsintCord)
                **🔎 Thank you for using OsintCord!**
            '''
        )
        if bot.user.avatar:
            embed.set_thumbnail(url=bot.user.avatar.url)

        await inter.response.send_message(embed=embed)
