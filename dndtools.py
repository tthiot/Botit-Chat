import discord
import re

async def roll(message):
  args = message.split(" ")
  if len(args) > 1:
    regex = "\d+d\d+"
    expr = re.match(regex, args[1], flags=0).group(1)
    qty = (expr.split("d"))[0]
    max = (expr.split("d"))[1]
  else:
    qty=1
    max=20
