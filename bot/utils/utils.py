import json
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

async def load_json_file(filename):
    try:
        async with aiofiles.open(filename, 'r') as f:
            json_str = await f.read()
            data = json.loads(json_str)
        return data
    except Exception as e:
        print('Error:', e)

async def dump_json_to_file(filename, data):
    try:
        async with aiofiles.open(filename, 'w') as f:
            json_str = json.dumps(data, indent=4)
            await f.write(json_str)
    except Exception as e:
        print('Error:', e)
