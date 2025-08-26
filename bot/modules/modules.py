import phonenumbers
import aiohttp

from phonenumbers import geocoder
from phonenumbers import carrier

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

async def check_phone_number(number):
    try:
        parsed_number = phonenumbers.parse(number, None)
        if not phonenumbers.is_valid_number(parsed_number):
            return {}
        geolocation = geocoder.description_for_number(parsed_number, 'en')
        carrier_ = carrier.name_for_number(parsed_number, 'en')
        country_code = phonenumbers.region_code_for_number(parsed_number)
        is_valid = phonenumbers.is_valid_number(parsed_number)
        return {
            'geolocation': geolocation,
            'carrier': carrier_,
            'country_code': country_code,
            'is_valid': is_valid
        }
    except Exception as e:
        print('Error:', e)
        return {}
