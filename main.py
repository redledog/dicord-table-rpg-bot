from discord.ext import commands
from Player import Player
import random
import Util
import Dialog
import ProcessErr as PE


client = commands.Bot(command_prefix='/')

# TODO players json파일로 옮겨야함
players = []


@client.event
async def on_ready():
    # client.get_all_channels()
    # client.guilds -> guilds(list) -> text_channels(list) -> members 안에 user
    # TODO 여기서 서버별 폴더 만들어주기 (유저데이터 넣을거임)
    client.remove_command('help')
    print(client.user.id)
    print("Bot Ready!")


@client.command('캐릭터생성')
async def create_character(ctx):
    if Util.exist_user(ctx.author, players):
        return
    else:
        player = Player(ctx.author)
        players.append(player)
        msg = Dialog.get_dialog('prologue').format(player.now_location, ctx.author.name)
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
    msg = Dialog.get_dialog('rollDice').format(ctx.author.name, dice)
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
