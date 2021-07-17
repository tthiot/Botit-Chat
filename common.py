import discord
from dotenv import load_dotenv
import os

load_dotenv()
MainPath = os.getenv('MAIN_PATH')

listCommand = ['$rollclass','$rollteam']

listCommandTitle = {}
listCommandArgs = {}
listCommandExemple = {}
listCommandDesc = {}

listCommandTitle["$rollclass"] = "$rollclass"
listCommandExemple["$rollclass"] = "$rollClass [Class Types] [-b]"
listCommandDesc["$rollclass"] =  "Chooses a random FFXIV class."
listCommandArgs["$rollclass"] = {
    "Class Types":"The types of class chosen, several categories can be chosen at once.\n possible values : DPS, Tank, Heal (different spelling accepted).",
    "-b" : "include Blue mage."
}

listCommandTitle["$rollteam"]="$rollteam"
listCommandExemple["$rollteam"] = "$rollteam [Party Type] [-u] [-b]"
listCommandDesc["$rollteam"] = "Makes a random team composition."
listCommandArgs["$rollteam"] = {
    "Party Type":"The type of party composition.\n possible values : Light, Full, Alliance \n defaut value : Light",
    "-u" : "Unique. No duplicate class.",
    "-b" : "include Blue mage."
}

async def helpCommand(message):
    args = message.content.split()
    content = discord.Embed()
    if(len(args) > 1):
        target = "$"+args[1].lower()
        if(target not in listCommand):
            await message.channel.send("Invalid command.")
            return
        else :
            title = listCommandTitle[target]
            content.add_field(name='Syntax',value=listCommandExemple[target], inline=False)
            content.add_field(name='Description',value=listCommandDesc[target], inline=False)
            for arg in listCommandArgs[target]:
                content.add_field(name=arg,value=listCommandArgs[target][arg], inline=False)

    else:
        title = "Commands"
        for command in listCommand:
            content.add_field(name=command,value=listCommandDesc[command],inline=False)
        
    content.title = title
    await message.channel.send(embed=content)