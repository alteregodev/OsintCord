import aiohttp

async def check_ip(ip):
    url = f'https://ipinfo.io/{ip}/json'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return {}
                data = await response.json()
                if not 'error' in data:
                    return data
                else:
                    return {}

    except Exception as e:
        print('Error:', e)
        return {}
