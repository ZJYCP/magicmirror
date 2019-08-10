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
        self.ser = serial.Serial(self.port, self.baud_rate)

