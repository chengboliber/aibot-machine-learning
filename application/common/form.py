# -*- coding:utf-8 -*-

from voluptuous import Schema, Required, All, Optional, Any

get_label = Schema({
    Required('dialogueContent'): All(str),
    Required('complainContent'): All(str),
    Required('complainType'): All(str)
})
