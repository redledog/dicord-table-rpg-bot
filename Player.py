import enum


# class PlayerState(enum):
#     NoneBattle = 1 << 1
#     OnBattle = 1 << 2


class Player:
    userId = ''
    level = 0
    curExp = ''
    nextExp = ''
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

    def __init__(self, author):
        self.userId = author.id
        self.level = 1
        for key in self.base_stat.keys():
            self.set_base_stat(key, 5)
        for key in self.combat_stat.keys():
            self.set_combat_stat(key, 100)

        # TODO 아래 위치 나중에 JSON 파일에서 빼서 넣어줄 것
        self.move('마을')

    def set_base_stat(self, stat, val):
        self.base_stat[stat] = val

    def set_combat_stat(self, stat, val):
        self.combat_stat[stat] = val

    def move(self, location):
        self.now_location = location
        
    # 플레이어 한마디 설정하는 함수
    def set_description(self, txt):
        self.description = txt

    def get_json(self):
        json_data = {
            'userId': f'{self.userId}',
            'level': f'{self.level}',
            'curExp': f'{self.curExp}',
            'nextExp': f'{self.nextExp}',
            'gold': f'{self.gold}',
            'now_location': f'{self.now_location}',
            'description': f'{self.description}',
            'skills': f'{self.skills}'
        }
        stat_dict = {}
        combat_stat_dict = {}
        inventory_list = []
        for key in self.base_stat.keys():
            stat_dict[key] = self.base_stat[key]

        for key in self.combat_stat.keys():
            combat_stat_dict[key] = self.combat_stat[key]

        for item in self.inventory:
            inventory_list.append(item)
        json_data['base_stat'] = stat_dict
        json_data['combat_stat'] = combat_stat_dict
        json_data['inventory'] = inventory_list

        return json_data
