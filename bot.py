import os
import discord
from dotenv import load_dotenv
import logging

# Provide .env file with following environment variables:
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
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
    print('Message Sent!')
    if str(message.channel) in CHANNELS:
        print(f'Message sent in monitored channel: {message.channel}') 

client.run(TOKEN)