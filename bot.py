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

async def informAuthor(message):
    author = message.author
    logging.info(f'Sending a message to {author} about deleted message')
    await author.create_dm()
    await author.dm_channel.send(
        f'Hi {author}, your message in #mod-releases was deleted. Only post ' \
        'links to mod releases! If you want to add a short description / '\
        'picture, you can post a message containing the link to the mod, '\
        'or edit an existing message.'
    )

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
        await informAuthor(message)

client.run(TOKEN)