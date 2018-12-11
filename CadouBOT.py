import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    print("Bot-ul este online pe Discord")
    await client.change_presence(game=discord.Game(name="Foloseste c!ajutor"))

@client.event
async def on_message(message):
    if message.content == 'c!cadou':
        variable = (
            '**1000credits de la Mosu @MadalinaMadaO_o#2657 iti va da:tada:**',
            '**Grad up de la Mosu:tada:**',
            '**Un băt de la Mosu :joy:**',
            '**Nimic :joy:**',
            '**Grad personalizat(ps: nu iti bag acces la ban kick etc..):tada:**',
            '**Ai primit HELPER de la Mosu :tada:**',
            '**Ai primit VIP de la Mosu :tada:**',
            '**Ai primit de la mosu o ciocolată :chocolate_bar: **',
            '**Ai primit de la mosu un pumn :punch:  **',
            '**O de dicatie speciala: https://www.youtube.com/watch?v=D3_2AIOEnZQ **',)
        await client.send_message(message.channel,(random.choice(variable)))




client.run('NTIwNjQ3NzY1Njc2NjU0NTky.Duw6yA.SHg6HXCZVEyHaVbGzTlzwDD5ZIY')
