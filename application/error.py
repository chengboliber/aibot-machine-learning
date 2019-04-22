# -*- coding:utf-8 -*-


class ServiceError(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return '<%d %s>' % (self.code, self.message)


ErrArgs = ServiceError(1000, '参数错误')
ErrLoginEmpty = ServiceError(1001, '用户未登录')

ErrInternal = ServiceError(2001, '内部错误')

