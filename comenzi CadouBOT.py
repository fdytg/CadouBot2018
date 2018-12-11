import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("Bot is online and connected to Discord")
@client.event
async def on_message(message):
    if message.content.startswith('!creator'):
        await client.send_message(message.channel,'<@%s>**Creatoarea Acestui Bot Este MadalinaMadaO_o#2657**'  %(message.author.id))
    if message.content.startswith('c!ajutor'):
        await client.send_message(message.channel,'**Comenzile Sunt : c!creator , c!invitebot , c!youtube , c!muzica , c!say , c!cadou **')
    if message.content.startswith('c!gucci'):
        await client.send_message(message.channel,'**Nu gucci fă îi guci**')
    if message.content.startswith('c!invitebot'):
        await client.send_message(message.channel,'**https://discordapp.com/oauth2/authorize?client_id=520647765676654592&scope=bot&permissions=8**')
    if message.content.startswith('c!muzica'):
        await client.send_message(message.channel,'**Intra drq pe https://www.youtube.com/ ii mai bun**')
    if message.content.startswith('c!youtube'):
        await client.send_message(message.channel,'**https://www.youtube.com/channel/UC2RzepBik-EhhIGXKomaS0Q?view_as=subscriber**')
    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        #args[0] = !SAY
        #args[1] = aolo
        #args[2] = fmm
        #args[1:] = ly
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))


client.run('NTIwNjQ3NzY1Njc2NjU0NTky.Duw6yA.SHg6HXCZVEyHaVbGzTlzwDD5ZIY') 
