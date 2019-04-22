# -*- coding:utf-8 -*-
import os

__version__ = '0.0.1'

web_root = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir))

DEBUG = False
HOST = '0.0.0.0'
PORT = 9091

DB_URI = 'mysql+pymysql://root:SmartCity@*6655@172.20.31.32:3306/flask_base'
DB_POOL_SIZE = 5
DB_POOL_RECYCLE = 5
DB_MAX_OVERFLOW = 10
DB_ECHO = False
