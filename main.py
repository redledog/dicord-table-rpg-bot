import discord

from Dungeon import Dungeon
from Player import Player

client = discord.Client()
players = []


@client.event
async def on_ready():
    print(client.user.id)
    print("Bot Ready!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content("접속"):
        startMsg = ''
        if exist_user(message.author):
            startMsg = f'돌아오신것을 환영합니다 {message.author}님'
        else:
            players.append(Player(message.author))
            startMsg = f'첫 접속을 환영합니다 {message.author}님'
        await message.channel.send(startMsg)
    if message.content.startswith("던전입장"):
        await Dungeon.enter(message)



def exist_user(author):
    for player in players:
        if player.userId == author:
            return True
    return False


key = str(input('Input Token >> '))

client.run(key)
