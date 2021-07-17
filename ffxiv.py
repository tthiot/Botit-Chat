import discord
import random
from random import randint
import json
import common

def randJsonArray(array):
  return array[randint(0,len(array)-1)]

async def rollclass(message):
  args = message.content.split()
  synTank = ["tank","tonc","tonk","tanque","tonq","tonque"]
  synDps = ["dps","dips","deeps"]
  synHeal = ["heal","heel","eel","il","hil","eal"]

  with open(common.MainPath+'ffxiv/classes.json') as json_file:
    data = json.load(json_file)
    classes = data['classes']
    if(len(args) > 1):
      possibilities = []
      lowStr = message.content.lower()
      if(any(classType in lowStr for classType in synDps)):
        possibilities+=classes['dps']
      if(any(classType in lowStr for classType in synHeal)):
        possibilities+=classes['heal']
      if(any(classType in lowStr for classType in synTank)):
        possibilities+=classes['tank']
      if '-b' in lowStr:
        possibilities.append(classes['Blue Mage'])

      #cas où pas de type de classe
      if(not any(classType in lowStr for classType in synDps) and not any(classType in lowStr for classType in synHeal) and not any(classType in lowStr for classType in synTank)):
        possibilities+=classes['dps']
        possibilities+=classes['heal']
        possibilities+=classes['tank']

      res = randJsonArray(possibilities)
    else:
      typeClassArray = ['tank','heal','dps']
      TypeClassRes = random.choice(typeClassArray)
      res = randJsonArray(classes[TypeClassRes])

    pic = res['picture']
    content = discord.Embed(title=res['name'],type="image",url=pic)
    content.set_image(url = pic)
    await message.channel.send(embed=content)

async def rollteam(message):
  args = message.content.split()
  with open(common.MainPath+'ffxiv/classes.json') as json_file:
    data = json.load(json_file) 
    classes = data['classes']

    possDPS = classes['dps']
    possHeal = classes['heal']
    possTank = classes['tank']
    unique = False

    #format :  [heal, tank, dps]
    switcher={
      "light":[1,1,2],
      "full":[2,2,4],
      "alliance": [2,1,5]
    }

    if(len(args) > 1):
      lowStr = message.content.lower()
      partyType='light'

      if 'light' in lowStr :
        partyType = 'light'
      if 'full' in lowStr :
        partyType = 'full'
      if 'alliance' in lowStr :
        partyType = 'alliance'
      tab = switcher.get(partyType,[1,1,2])
      comptitle = partyType[0].upper() + partyType[1:]

      if '-b' in lowStr:
        possDPS.append(classes['Blue Mage'])
        possHeal.append(classes['Blue Mage'])
        possTank.append(classes['Blue Mage'])
      
      if '-u' in lowStr:
        unique = True

    else:
      tab = switcher.get("light")
      comptitle = "Light"

    content = discord.Embed(title=comptitle+" Party Composition                                                                                                             \u200B")
    res = []
    #Heals
    for i in range(tab[0]):
      varclass = randJsonArray(possHeal)
      if(unique):
        while(varclass['name'] in res):
          varclass = randJsonArray(possHeal)
        res.append(varclass['name'])
      content.add_field(name="Heal", value=varclass['name'], inline=True)
    
    column = tab[0]%3
    while(column<3):
      content.add_field(name='\u200B',value='\u200B',inline=True)
      column+=1

    #Tanks
    for i in range(tab[1]):
      varclass = randJsonArray(possTank)
      if(unique):
        while(varclass['name'] in res):
          varclass = randJsonArray(possTank)
        res.append(varclass['name'])
      content.add_field(name="Tank", value=varclass['name'], inline=True)

    column = tab[1]%3
    while(column<3):
      content.add_field(name='\u200B',value='\u200B',inline=True)
      column+=1

    #DPS
    for i in range(tab[2]):
      varclass = randJsonArray(possDPS)
      if(unique):
        while(varclass['name'] in res):
          varclass = randJsonArray(possDPS)
        res.append(varclass['name'])
      content.add_field(name="DPS", value=varclass['name'], inline=True)

    column = tab[2]%3
    while(column<3):
      content.add_field(name='\u200B',value='\u200B',inline=True)
      column+=1

    await message.channel.send(embed=content)