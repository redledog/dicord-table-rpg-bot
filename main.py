from discord.ext import commands
from Player import Player
import random
import Util
import ProcessErr as PE


client = commands.Bot(command_prefix='/')

# TODO players json파일로 옮겨야함
players = []


@client.event
async def on_ready():
    print(client.user.id)
    print("Bot Ready!")


@client.command('캐릭터생성')
async def create_character(ctx):
    if Util.exist_user(ctx.author, players):
        return
    else:
        player = Player(ctx.author)
        players.append(player)
        msg = f'눈을 뜬 당신은 어느새 "{player.now_location}" 안에 있다는 것을 깨달았습니다. \n'
        msg = msg + f'"{ctx.author.name}"... 어렴풋이 떠오르는 것은 당신의 이름뿐이었습니다.'
    await ctx.send(Util.change_font_cs(msg))


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
        if not parse[0] or parse[1] < 2:
            return await ctx.send(PE.wrong_command())
        else:
            dice = random.randrange(1, parse[1]+1)
    msg = f'{ctx.author.name}님이 주사위를 굴립니다.\n나온 수는 [{dice}] 입니다!'
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
