from flask import request, Blueprint
from application.controller import route
from machine_learning_label import label
from application.common import form


bp = Blueprint('Label', __name__, url_prefix='/machine_learn/Label')


@route(bp, '/getLabel', methods=['POST'])
def get_label():
    """
    打标签
    :param dialogueContent:  对话文本内容
    :param complain_content: 工单投诉内容
    :param complain_type: 投诉类型
    :return:
    """
    params = form.get_label(request.get_json(force=True))
    dialogue_content = params['dialogueContent']
    complain_content = params['complainContent']
    complain_type = params['complainType']
    result = label.get_label(dialogue_content=dialogue_content, complain_content=complain_content,
                             complain_type=complain_type)
    return result
