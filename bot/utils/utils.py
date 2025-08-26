import disnake
import aiofiles
from disnake.ext import commands

async def get_error_embed(error: str):
        embed = disnake.Embed(
            title='Error',
            description=error
        )
        return embed

async def get_file_content(filename):
    async with aiofiles.open('.version', 'r') as f:
        content = await f.read()
    return content


