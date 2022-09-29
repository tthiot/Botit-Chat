import discord
import random
import os
import pathlib
import ffxiv
import dndtools
import stuff
import common
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
  await client.user.edit(username='Botit chat')
  print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    if message.content.startswith('$rollclass'):
      await ffxiv.rollclass(message)
    if message.content.startswith('$rollteam'):
      await ffxiv.rollteam(message)
       
    if message.content.startswith('!roll'):
      await dndtools.roll(message)

    if message.content.lower().startswith(tuple(stuff.synEnvol)):
      await stuff.jmanvol(message)

    if message.content.lower().startswith('niaou'):
      await stuff.niaou(message)

    if message.content.lower().startswith("$command"):
      await common.helpCommand(message)

    if message.content.startswith("!testembed"):
      embed=discord.Embed(title="test", url="testurl", description="testDescription", color=discord.Color.blue())
      await message.channel.send(embed=embed)



my_secret = os.getenv('DISCORD_TOKEN')
client.run(my_secret)

