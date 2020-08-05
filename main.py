from discord.ext import commands
from Player import Player
import random


client = commands.Bot(command_prefix='/')
players = []


@client.event
async def on_ready():
    print(client.user.id)
    print("Bot Ready!")


@client.command('접속')
async def connect(ctx):
    if exist_user(ctx.author):
        hello_msg = change_font_css(f'돌아오신것을 환영합니다 {ctx.author}님')
    else:
        players.append(Player(ctx.author))
        hello_msg = change_font_css(f'첫 접속을 환영합니다 {ctx.author}님')
    await ctx.send(hello_msg)


def exist_user(author):
    for player in players:
        if player.userId == author:
            return True
    return False


@client.command('이동')
async def moveto(ctx):
    # TODO 맵이동 커맨드 작성
    await ctx.send(change_font_css('공사중...'))


@client.command('주사위')
async def roll_dice(ctx, arg=None):
    print(ctx)
    if not arg:
        dice = random.randrange(1, 7)
    else:
        parse = try_parse(int, arg)
        if not parse[0]:
            return await ctx.send(wrong_command())
        else:
            dice = random.randrange(1, parse[1]+1)
    msg = f'{ctx.author}님이 주사위를 굴립니다.\n나온 수는 [{dice}] 입니다!'
    msg = change_font_css(msg)
    await ctx.send(msg)


# 잘못된 명령어입력시 작동하게할 함수
def wrong_command():
    return '잘못된 명령어 입니다.'


# 특정타입으로 parsing하는 함수
def try_parse(parse_type, arg):
    try:
        parse_arg = parse_type(arg)
    except ValueError as e:
        print('\033[31m' + f'예외 발생 : {e}' + '\033[0m')
        return False, None
    return True, parse_arg


# 디스코드 내부기능 폰트관련 설정
def change_font_css(msg):
    return f'```css\n {msg}\n```'


# 디스코드 토큰 텍스트파일이 있다면 가져오기
# 없으면 직접입력
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
