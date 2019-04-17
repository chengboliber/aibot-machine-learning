from application import app
from application.util.exception import try_except
from machine_learning_label import label
from flask import request, jsonify


@app.route('/getLabel', methods=['POST', 'GET'])
@try_except
def get_label():
    """
    打标签
    :param dialogueContent:  对话文本内容
    :param complain_content: 工单投诉内容
    :param complain_type: 投诉类型
    :return:
    """
    params = request.get_json(force=True)
    dialogue_content = params['dialogueContent']
    complain_content = params['complainContent']
    complain_type = params['complainType']
    result = label.get_label(dialogue_content=dialogue_content, complain_content=complain_content,
                             complain_type=complain_type)
    return jsonify(result)
