import discord
from discord.ext import commands
import requests
import random

bot = commands.Bot(command_prefix='$', intents=discord.Intents().all())


@bot.command('randommem')
async def randommem(ctx):
    a = ['project/mem1.jpg', 'project/mem2.jpg', 'project/mem3.jpg']
    b = random.randint(0, 2)
    with open(a[b], 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command('mem')
async def mem(ctx):
    with open('project/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command('motivation')
async def cute(ctx):
    a = ['Ты лучший', 'У тебя всё получится', 'Удачи тебе']
    b = random.randint(0, 2)
    await ctx.reply(a[b])
    c = ['project/cat1.jpg', 'project/cat2.jpg', 'project/cat3.jpg',
         'project/cat4.jpg', 'project/cat5.jpg',]
    d = random.randint(0, 4)
    with open(c[d], 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run('TOKEN HERE')
