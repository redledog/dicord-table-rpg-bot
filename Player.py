

class Player:
    userId = ''
    level = 0
    base_stat = {
        'str': -1,
        'con': -1,
        'int': -1,
        'wis': -1,
        'agi': -1,
        'luk': -1,
    }
    # combat_stat = {
    #     '':'',
    #     '': '',
    # }
    now_location = ''
    skills = []
    inventory = []
    description = ''

    def __init__(self, author):
        self.userId = author.id
        self.level = 1
        for key in self.base_stat.keys():
            self.set_base_stat(key, 10)
        # TODO 여기에 전투 스텟 정의

        # TODO 아래 위치 나중에 JSON 파일에서 빼서 넣어줄 것
        self.move('마을')

    def set_base_stat(self, stat, val):
        self.base_stat[stat] = val

    def move(self, location):
        self.now_location = location
        
    # 플레이어 한마디 설정하는 함수
    def set_description(self, txt):
        self.description = txt
