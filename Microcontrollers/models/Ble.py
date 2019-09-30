#!/usr/bin/env python
# encoding: utf-8
"""
@author: Glyn
@contact: chnzjycp@foxmail.com
@file: Ble.py
@time: 19-8-5 下午4:51
@desc:蓝牙通信模块
"""

import serial
import time
import threading


class BLE:
    port = ''
    baud_rate = 115200

    def __init__(self):
        # self.ser = serial.Serial(self.port, self.baud_rate)
        self.sensors = []
        self.listen_msg()

    # 监听
    def listen_msg(self):
        data = {'code': 1,'data': '1111'}
        if True:
            self.notifySensor(data)

    # 通知
    def notifySensor(self, data):
        for i, sensor in enumerate(self.sensors):
            sensor.update(data)

    # 添加传感器
    def attach(self, sensor):
        self.sensors.append(sensor)


if __name__ == 'main':
    blue = BLE()
    blue.listen_msg()
