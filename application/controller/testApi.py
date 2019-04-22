from flask import request, jsonify, Blueprint

from application.controller import route
from application.middles import testMiddle as m

bp = Blueprint('test', __name__, url_prefix='/machine_learn/interface_test')


@route(bp, '/get_test_info', methods=['POST'])
def get_test_info():
    params = request.get_json(force=True)
    result = m.get_test(**params)
    return jsonify({'success': True, 'res': result})




