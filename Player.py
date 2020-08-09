import Util
import json
import discord
import enum

# class PlayerState(enum):
#     NoneBattle = 1 << 1
#     OnBattle = 1 << 2


class Player:
    #region 플레이어 정보
    userId = ''
    userName = ''
    level = 1
    curExp = 0
    nextExp = 10
    gold = 0
    now_location = ''
    description = ''
    base_stat = {
        'str': -1,
        'con': -1,
        'int': -1,
        'wis': -1,
        'agi': -1,
        'luk': -1,
    }
    combat_stat = {
        'curHP': -1,
        'maxHP': -1,
        'curMP': -1,
        'maxMP': -1
    }
    skills = 0
    inventory = []
    command_permission = 0
    #endregion
    
    # __init__ 대신 쓸 초기화 함수
    def init_player(self, author):
        self.userId = author.id
        self.userName = author.name
        self.level = 1
        for key in self.base_stat.keys():
            self.set_base_stat(key, 5)
        for key in self.combat_stat.keys():
            self.set_combat_stat(key, 100)

        # TODO 아래 위치 나중에 JSON 파일에서 빼서 넣어줄 것
        self.move('마을')
        return self

    def set_base_stat(self, stat, val):
        self.base_stat[stat] = val

    def set_combat_stat(self, stat, val):
        self.combat_stat[stat] = val

    def move(self, location):
        self.now_location = location

    # 해당 Player 객체를 json 형태로 변환해서 리턴
    def get_json(self):
        json_data = {
            'userId': self.userId,
            'userName': self.userName,
            'level': self.level,
            'curExp': self.curExp,
            'nextExp': self.nextExp,
            'gold': self.gold,
            'now_location': self.now_location,
            'description': self.description,
            'skills': self.skills,
            'base_stat': self.base_stat,
            'combat_stat': self.combat_stat,
            'inventory': self.inventory,
            'command_permission': self.command_permission
        }
        return json_data

    # Json 파일로 부터 player 객체 생성
    def from_json(self, json_data):
        self.userId = json_data['userId']
        self.userName = json_data['userName']
        self.level = json_data['level']
        self.curExp = json_data['curExp']
        self.nextExp = json_data['nextExp']
        self.gold = json_data['gold']
        self.now_location = json_data['now_location']
        self.description = json_data['description']
        self.skills = json_data['skills']
        self.base_stat = json_data['base_stat']
        self.combat_stat = json_data['combat_stat']
        self.inventory = json_data['inventory']
        self.command_permission = json_data['command_permission']
        return self

    # discord.Embed 객체 반환
    def show_base_info(self):
        embed = discord.Embed(
            title=f'{self.userName}님의 기본정보',
            description=f'레벨: [ {self.level} ]\n체력: [ {self.combat_stat["curHP"]} / {self.combat_stat["maxHP"]} ]\n'
                        + f'마력: [ {self.combat_stat["curMP"]} / {self.combat_stat["maxMP"]} ]\n'
                        + f'경험치: [ {self.curExp} / {self.nextExp} ]\n'
                        + f'한마디 : {self.description}',
            color=discord.Color.dark_red()
        )
        return embed


JSON_PATH = './Servers/{0}/UserData.json'


def check_exist_user(guild, author):
    json_path = JSON_PATH.format(guild.id)
    if not Util.check_file_exists(json_path):
        return False
    with open(json_path, 'r') as users_json:
        user_list = json.load(users_json)
    if user_list['UserList'][f'{author.id}']:
        return True
    return False


def create_player_data(guild, player):
    json_path = JSON_PATH.format(guild.id)
    if not Util.check_file_exists(json_path):
        with open(json_path, 'w') as user_json:
            init_user_list = {f'{player.userId}': player.get_json()}
            init_json = {'UserList': init_user_list}
            Util.json_dump(init_json, user_json)
    else:
        with open(json_path, 'w') as user_list:
            users = json.load(user_list)
            users['UserList'][f'{player.userId}'] = player.get_json()
            Util.json_dump(users, user_list)


def update_player_data(guild, player):
    json_path = JSON_PATH.format(guild.id)
    with open(json_path, 'w') as user_list:
        users = json.load(user_list)
        users['UserList'][f'{player.userId}'] = player.get_json()
        Util.json_dump(users, user_list)


def get_player_data(guild, author):
    json_path = JSON_PATH.format(guild.id)
    with open(json_path, 'r') as user_list:
        users = json.load(user_list)
    return users['UserList'][f'{author.id}']
