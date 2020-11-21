import os
import discord
from dotenv import load_dotenv
import logging

# Provide .env file with following environment variables:
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_NAME')
LOGLEVEL = str(os.getenv('LOGLEVEL'))
CHANNELS = str(os.getenv('MONITORED_CHANNELS')).split(",") 

# https://docs.python.org/3/library/logging.html#logging-levels
logging.basicConfig(level=LOGLEVEL)

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} connected to:\n'
            f'{guild.name}(id: {guild.id})\n'
            'And monitoring channels:\n'
            f'{CHANNELS}'
        )

@client.event
async def on_message(message):
    hyperlinks = ['https://', 'http://']
    if str(message.channel) in CHANNELS:
        logging.info(f'Message sent in monitored channel: {message.channel}') 
    else:
        logging.info(f'Message sent in channel: {message.channel} - ignoring')
        return
    if any(linkStart in message.content.lower() for linkStart in hyperlinks):
        logging.info('Message contains a link!')
    else:
        logging.info('Message does not contain a link - deleting..')
        await message.delete(delay = 2)

client.run(TOKEN)