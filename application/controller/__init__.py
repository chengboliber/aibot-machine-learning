# -*- coding:utf-8 -*-

import traceback
import pkgutil
import importlib
from functools import wraps
from flask import request, Blueprint
from voluptuous import MultipleInvalid
from werkzeug import exceptions as wkerr

from application.util import jsonify
from application import error as err


def route(app, *args, **kwargs):
    def decorator(func):
        @app.route(*args, **kwargs)
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                rv = func(*args, **kwargs)
            except (wkerr.BadRequest, MultipleInvalid) as e:
                print(str(e))
                return jsonify(request.path, has_error=True, data=err.ErrArgs)
            except err.ServiceError as e:
                return jsonify(request.path, has_error=True, data=e)
            except Exception:
                print(traceback.format_exc())
                return jsonify(request.path, has_error=True, data=err.ErrInternal)

            return jsonify(request.path, data=rv)

        return func
    return decorator


def register_blueprints(app):
    for _, name, _ in pkgutil.iter_modules(__path__):
        m = importlib.import_module("%s.%s" % (__name__, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
    return app
