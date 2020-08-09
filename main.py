from discord.ext import commands
from Player import Player
import Player as _Player
import random
import Util
import Dialog
import ProcessErr as PE


client = commands.Bot(command_prefix='/')


@client.event
async def on_ready():
    # 유저 데이터 보관용 서버별 폴더 생성
    for guild in client.guilds:
        Util.create_folder(f'./Servers/{guild.id}')
    client.remove_command('help')
    print(client.user.id)
    print("Bot Ready!")


@client.command('캐릭터생성')
async def create_character(ctx):
    if _Player.check_exist_user(ctx.guild, ctx.author):
        return
    player = Player().init_player(ctx.author)
    _Player.create_player_data(ctx.guild, player)
    msg = Dialog.get_dialog('prologue').format(player.now_location, ctx.author.name)
    await ctx.send(Util.change_font_cs(msg))


@client.command('정보')
async def show_user_info(ctx):
    if not _Player.check_exist_user(ctx.guild, ctx.author):
        return
    player = Player().from_json(_Player.get_player_data(ctx.guild, ctx.author))
    await ctx.send(embed=player.show_base_info())


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
