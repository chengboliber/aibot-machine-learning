# -*- coding:utf-8 -*-
import time

from flask import jsonify as flask_jsonify
from flask import request

from application.config.default_config import __version__
from application import error as err
from application import app


def jsonify(interface, has_error=False, data=None):
    out = {
        '_head': {
            '_version': __version__,
            '_msgType': 'response',
            '_interface': interface,
            '_remark': '',
            '_timestamps': int(time.time())
        },
        '_data': {
            '_errCode': None,
            '_errStr': None,
            '_ret': None
        }
    }

    if has_error:
        out['_data']['_errCode'] = data.code
        out['_data']['_errStr'] = data.message
        out['_data']['_ret'] = -1
    else:
        out['_data']['_errCode'] = 0
        out['_data']['_errStr'] = 'ok'
        out['_data']['_ret'] = 0
        if data is not None:
            out['_data']['retData'] = data
    return flask_jsonify(out)


def validate_args(in_data):
    """
    参数验证
    :param in_data:
    :return:
    """
    if app.debug:
        print('<%s> <%s>' % (request.path, str(in_data)))

    if in_data is None:
        return dict()

    if not isinstance(in_data, dict):
        raise err.ErrArgs

    if in_data.get('_head') is None:
        raise err.ErrArgs

    if in_data['_head'].get('_version') is None:
        raise err.ErrArgs

    if __version__ != in_data['_head']['_version']:
        raise err.ErrArgs

    if in_data.get('_param') is None or \
            not isinstance(in_data['_param'], dict):
        raise err.ErrArgs

    return in_data['_param']


def validate_args_with_check_login(data):
    """
    验证登陆模块暂时不用
    :param data:
    :return:
    """
    params = validate_args(data)

    token = params.pop('loginToken') if 'loginToken' in params else None
    uid = params.pop('loginUserId') if 'loginUserId' in params else None

    if not (token or uid):
        raise err.ErrLoginEmpty

    return params

