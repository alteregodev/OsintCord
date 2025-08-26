import re
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
    try:
        async with aiofiles.open(filename, 'r') as f:
            content = await f.read()
        return content
    except Exception as e:
        print('Error:', e)

async def is_valid_ip(ip):
    pattern = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return bool(pattern.fullmatch(ip))
