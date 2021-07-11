import discord
import random
import requests
import os

pics = ["https://i.pinimg.com/originals/3e/0c/9d/3e0c9d4bd9caa0e74bd381d8289d0627.jpg",
"https://i.ytimg.com/vi/3oem-M2tQU4/maxresdefault.jpg",
"https://i.pinimg.com/originals/1e/16/d5/1e16d586ae460fb175bc428ffb738592.jpg",
"https://external-preview.redd.it/b5uCk9uoIURB6yepJ9cDvm2N9mUtKYC1cLKQCV_3aeQ.jpg?auto=webp&s=4457b792c24c3e77f9c07f2c9d193986a14fce78",
"https://st4.depositphotos.com/9043150/29902/i/600/depositphotos_299027022-stock-photo-cute-gray-cat-toy-car.jpg",
"https://i.imgur.com/Q0Nd58g.jpg"]
synEnvol = ["jmanvole","jmenvole","j'manvole","j'menvole","jmanvol","jmenvol","j'manvol","j'menvol"]

async def jmanvol(message):
    res = random.choice(pics)
    r = requests.get(res, allow_redirects=False)
    open('jmanvol.jpg','wb+').write(r.content)
    with open('jmanvol.jpg', 'rb') as f:
        picture = discord.File(f)
        await message.channel.send(file=picture)
    os.remove(path='jmanvol.jpg')

async def niaou(message):
    with open('pictures/niaou.png','rb') as f:
        picture = discord.File(f)
        await message.channel.send(file=picture)