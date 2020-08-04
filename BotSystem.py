
from Player import Player
from main import exist_user, players, client


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
        return str('Test')
