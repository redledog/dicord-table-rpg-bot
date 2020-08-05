from discord.ext import commands
from Player import Player
import random
import Util
import ProcessError as PE


client = commands.Bot(command_prefix='/')
players = []


@client.event
async def on_ready():
    print(client.user.id)
    print("Bot Ready!")


@client.command('접속')
async def connect(ctx):
    if Util.exist_user(ctx.author, players):
        hello_msg = Util.change_font_css(f'돌아오신것을 환영합니다 {ctx.author}님')
    else:
        players.append(Player(ctx.author))
        hello_msg = Util.change_font_css(f'첫 접속을 환영합니다 {ctx.author}님')
    await ctx.send(hello_msg)


@client.command('이동')
async def moveto(ctx):
    # TODO 맵이동 커맨드 작성
    await ctx.send(Util.change_font_css('공사중...'))


@client.command('주사위')
async def roll_dice(ctx, arg=None):
    if not arg:
        dice = random.randrange(1, 7)
    else:
        parse = Util.try_parse(int, arg)
        if not parse[0]:
            return await ctx.send(PE.wrong_command())
        else:
            dice = random.randrange(1, parse[1]+1)
    msg = f'{ctx.author}님이 주사위를 굴립니다.\n나온 수는 [{dice}] 입니다!'
    msg = Util.change_font_css(msg)
    await ctx.send(msg)


# 디스코드 토큰 텍스트파일이 있다면 가져오기
# 없으면 직접입력
token = ''
try:
    f = open('token.txt', 'r')
    token = f.readline()
except FileNotFoundError:
    PE.show_error(FileNotFoundError)
else:
    f.close()

if not token:
    key = str(input('Input Token >> '))
else:
    key = token

client.run(key)
