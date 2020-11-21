import os

import discord
from dotenv import load_dotenv

# Provide .env file with following environment variables:
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to:\n'
            f'{guild.name}(id: {guild.id})\n'
        )

client.run(TOKEN)