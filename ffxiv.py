import discord
import random

classes = ["Astrologian","Scholar","White Mage", "Dark Knight", "Gunbreaker", "Paladin", "Warrior", "Dragoon", "Monk", "Ninja", "Samuraï", "Bard", "Dancer", "Machinist", "Black Mage", "Summoner", "Red Mage"]
classesDPS = ["Dragoon", "Monk", "Ninja", "Samuraï", "Bard", "Dancer", "Machinist", "Black Mage", "Summoner", "Red Mage"]
classesHeal=["Astrologian","Scholar","White Mage"]
classesTank=["Dark Knight", "Gunbreaker", "Paladin", "Warrior"]

pictures = {"Astrologian":"https://i.pinimg.com/736x/93/39/ad/9339ada3427531456bf02f6d729bdba8.jpg",
"Scholar":"https://d3fa68hw0m2vcc.cloudfront.net/980/231785232.jpeg",
"White Mage":"https://i.pinimg.com/564x/2b/9e/3a/2b9e3a1feac3d7909b1a09fd7a6e437a.jpg", "Dark Knight":"https://d3fa68hw0m2vcc.cloudfront.net/4d5/231785226.jpeg",
"Gunbreaker":"https://img.finalfantasyxiv.com/t/a8e125b33aac63733a069388f371e10cc5baeba1_9.jpg?1576631760", "Paladin":"https://d3fa68hw0m2vcc.cloudfront.net/0d3/231610520.jpeg",
"Warrior" : "https://d3fa68hw0m2vcc.cloudfront.net/bb1/231594019.jpeg",
"Dragoon":"https://d3fa68hw0m2vcc.cloudfront.net/53f/231610526.jpeg",
"Monk":"https://d3fa68hw0m2vcc.cloudfront.net/107/231594040.jpeg",
"Ninja":"https://d3fa68hw0m2vcc.cloudfront.net/5ac/231610534.jpeg",
"Samuraï":"https://d3fa68hw0m2vcc.cloudfront.net/c39/231698977.jpeg",
"Bard":"https://i.pinimg.com/736x/38/de/85/38de85980f16de2c493534c1f00ce3eb.jpg", 
"Dancer":"https://cdn-prod.scalefast.com/public/assets/img/resized/squareenix-store-v3/1fc445b8e5693360d298171b63d5cba4_640_640_Q10.jpg", 
"Machinist":"https://d3fa68hw0m2vcc.cloudfront.net/6f9/231594054.jpeg", 
"Black Mage":"https://d3fa68hw0m2vcc.cloudfront.net/436/231594061.jpeg", 
"Summoner":"https://d3fa68hw0m2vcc.cloudfront.net/5ef/231610548.jpeg", 
"Red Mage":"https://cdn-prod.scalefast.com/public/assets/user/1614900/image/1d5005fc60d14a6870abb9d1ba33c8c2.jpg",
"Blue Mage":"https://steamuserimages-a.akamaihd.net/ugc/945095565208555226/F64AE807633AEE2017EA4C2864E8AA26670BEBC5/"
}

async def rollclass(message):
  args = message.content.split()
  synTank = ["tank","tonc","tonk","tanque","tonq","tonque"]
  synDps = ["dps","dips","deeps"]
  synHeal = ["heal","heel","eel","il","hil","eal"]

  if(len(args) > 1):
    possibilities = []
    lowStr = message.content.lower()
    if(any(classType in lowStr for classType in synDps)):
      possibilities+=classesDPS
    if(any(classType in lowStr for classType in synHeal)):
      possibilities+=classesHeal
    if(any(classType in lowStr for classType in synTank)):
      possibilities+=classesTank
    if '-b' in lowStr:
      possibilities.append("Blue Mage")

    res = random.choice(possibilities)
  else:
      res = random.choice(classes)

  pic = pictures[res]
  content = discord.Embed(title=res,type="image",url=pic)
  content.set_image(url = pic)
  await message.channel.send(embed=content)

async def rollteam(message):
  args = message.content.split()
  possDPS = classesDPS[:]
  possHeal = classesHeal[:]
  possTank = classesTank[:]
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
      possDPS.append('Blue Mage')
      possHeal.append('Blue Mage')
      possTank.append('Blue Mage')
    
    if '-u' in lowStr:
      unique = True

  else:
    tab = switcher.get("light")
    comptitle = "Light"
  

  content = discord.Embed(title=comptitle+" Party Composition                                                                                                             \u200B")
  res = []
  #Heals
  for i in range(tab[0]):
    varclass = random.choice(possHeal)
    if(unique):
      while(varclass in res):
        varclass = random.choice(possHeal)
      res.append(varclass)
    content.add_field(name="Heal", value=varclass, inline=True)
  
  column = tab[0]%3
  while(column<3):
    content.add_field(name='\u200B',value='\u200B',inline=True)
    column+=1

  #Tanks
  for i in range(tab[1]):
    varclass = random.choice(possTank)
    if(unique):
      while(varclass in res):
        varclass = random.choice(possTank)
      res.append(varclass)
    content.add_field(name="Tank", value=varclass, inline=True)

  column = tab[1]%3
  while(column<3):
    content.add_field(name='\u200B',value='\u200B',inline=True)
    column+=1

  #DPS
  for i in range(tab[2]):
    varclass = random.choice(possDPS)
    if(unique):
      while(varclass in res):
        varclass = random.choice(possDPS)
      res.append(varclass)
    content.add_field(name="DPS", value=varclass, inline=True)

  column = tab[2]%3
  while(column<3):
    content.add_field(name='\u200B',value='\u200B',inline=True)
    column+=1

  await message.channel.send(embed=content)