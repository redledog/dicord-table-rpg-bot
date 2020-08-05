import ProcessError as PE


# 이미 존재하는 유저판별
def exist_user(author, players):
    for player in players:
        if player.userId == author:
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


# 디스코드 내부기능 폰트관련 설정
def change_font_css(msg):
    return f'```css\n {msg}\n```'