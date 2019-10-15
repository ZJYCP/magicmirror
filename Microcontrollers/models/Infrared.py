#!/usr/bin/env python
# encoding: utf-8
"""
@author: Glyn
@contact: chnzjycp@foxmail.com
@file: Infrared.py
@time: 19-9-30 上午11:02
@desc: 红外模块 //fix:所有远端传感器
"""

from models.Ble import BLE
from utils.logger import *
import requests


class Infraed:
    def __init__(self, ble):
        self.ble = ble
        self.ble.attach(self)

    def update(self, data):
        url = 'http://baidu.com'

        if data['data'] == 1:
            url = "http://mirror.com/api/micro/alarm/infrared"
        response = requests.get(url)
        print(response)




class Fires:
    def __init__(self, ble):
        self.ble = ble
        self.ble.attach(self)

    def update(self, data):
        url = 'http://baidu.com'

        if data['data'] == 1:
            url = "http://mirror.com/api/micro/alarm/infrared"
        response = requests.get(url)
        print(response)


def start():
    logger.debug('start 远端传感器')
    bl = BLE()
    inf = Infraed(bl)
    fire=Fires(bl)
    bl.listen_msg()
