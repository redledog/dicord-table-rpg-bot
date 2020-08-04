import discord

import Dungeon
from Player import Player
import BotSystem

client = discord.Client()
players = []


@client.event
async def on_ready():
    print(client.user.id)
    print("Bot Ready!")


@client.event
async def on_disconnect():
    client.get_channel().send('봇 종료')
    print("Bot off!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = await process_message(message)
    if not msg:
        return
    else:
        await message.channel.send(msg)


def exist_user(author):
    for player in players:
        if player.userId == author:
            return True
    return False


@client.event
async def process_message(message):
    if message.content == '/접속':
        if exist_user(message.author):
            hello_msg = f'돌아오신것을 환영합니다 {message.author}님'
        else:
            players.append(Player(message.author))
            hello_msg = f'첫 접속을 환영합니다 {message.author}님'
        return hello_msg
    if message.content.startswith("던전입장"):
        return Dungeon.enter(message)


try:
    f = open('token.txt', 'r')
    token = f.readline()
finally:
    f.close()

if not token:
    key = str(input('Input Token >> '))
else:
    key = token

client.run(key)
