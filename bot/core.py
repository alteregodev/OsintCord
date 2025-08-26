##################################################################################################################################
# Copyright - alteregodev                                                                                                        #
# Github - https://github.com/alteregodev/OsintCord                                                                              #
# OsintCord is a powerful discord bot made for OSINT investigations and retrieving information about user profiles or guilds     #
##################################################################################################################################

import disnake
from dotenv import load_dotenv
from os import getenv
from disnake.ext import commands

from commands.commands import load

def main():
    load_dotenv()
    BOT_TOKEN = getenv('BOT_TOKEN')

    intents = disnake.Intents.default()
    bot = commands.Bot(command_prefix='?', intents=intents) # The command prefix is unused, since this is a slash command bot

    load(bot)
    bot.run(BOT_TOKEN)

if __name__ == '__main__':
    main()

