import ProcessErr as PE
import json
import os


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


# 폴더 생성 함수
def create_folder(directory):
    try:
        if not check_file_exists(directory):
            os.makedirs(directory)
    except OSError:
        PE.show_error(OSError)


# 파일 존재 여부 확인 함수
def check_file_exists(path):
    return os.path.exists(path)


# Json Dump 랩핑
def json_dump(obj, fp):
    json.dump(obj, fp, indent=4, ensure_ascii=False)
