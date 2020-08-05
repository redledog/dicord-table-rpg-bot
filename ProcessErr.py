#import sys


commandID = {
    1:'정보',
    2:'이동',

}

# 잘못된 명령어입력시 작동하게할 함수
def wrong_command():
    return '잘못된 명령어 입니다.'

# 예외발생 메세지
def show_error(err):
    print('\033[31m' + f'예외 발생 : {err}' + '\033[0m')
    #print('\033[31m' + f'예외 발생 : {sys.exc_info()[0].args}' + '\033[0m')