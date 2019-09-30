#!/usr/bin/env python
# encoding: utf-8
"""
@author: Glyn
@contact: chnzjycp@foxmail.com
@file: Infrared.py
@time: 19-9-30 上午11:02
@desc: 红外模块
"""

from models.Ble import BLE
from utils.logger import *


class Infraed:
    def __init__(self, ble):
        self.ble = ble
        self.ble.attach(self)

    def update(self, data):
        # 数据库操作
        target = 1
        if target == 1:
            logger.debug(data)


class Fire:
    pass


def start():
    logger.debug('start inf')
    bl = BLE()
    inf = Infraed(bl)
    bl.listen_msg()
