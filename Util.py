import ProcessErr as PE
import json


# 이미 존재하는 유저판별
def exist_user(author, players):
    for player in players:
        if player.userId == author.id:
            return True
    return False


# 특정타입으로 parsing 하는 함수
def try_parse(parse_type, arg):
    try:
        parse_arg = parse_type(arg)
    except ValueError:
        PE.show_error(ValueError)
        return False, None
    return True, parse_arg


# region 디스코드 마크업 관련 함수들
def change_font_css(msg):
    return f'```css\n{msg}\n```'


def change_font_cs(msg):
    return f'```cs\n{msg}\n```'


def change_font_diff(msg):
    return f'```diff\n{msg}\n```'
# endregion


# JSON 불러오기
def get_json_data(file_name):
    with open(f'./JsonData/{file_name}.json', 'r') as json_data:
        return json.load(json_data)
