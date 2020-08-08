#TODO 게임중 출력되는 문자열 가지고 있을 장소
import Util


def get_dialog(dialog_id):
    # if len(dialog_data) <= 0:
    #     init_dialog()
    return Util.get_json_data('DialogData')[dialog_id]
    # return dialog_data[dialog_id]


# def init_dialog():
#     with open('./JsonData/DialogData.json', 'r') as json_data:
#         return json.load(json_data)
#
#
# def get_dialog_data():
#     with open('./JsonData/DialogData.json', 'r') as json_data:
#         return json.load(json_data)

# dialog_data = init_dialog()
