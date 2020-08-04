

class Dungeon:
    players = []

    def enter(self, message):
        self.players.append(message.author)
        message.channel.send(f'{message.author}님 던전에 입장했습니다.')