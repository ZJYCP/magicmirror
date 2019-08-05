#!/usr/bin/env python
# encoding: utf-8
"""
@author: Glyn
@contact: chnzjycp@foxmail.com
@file: TempHumid.py
@time: 19-8-5 下午12:59
@desc: 温湿度传感器控制类
"""

import sys
import traceback
import logging as _logging


class TempHumid:
    pin = 5

    def __init__(self):
        pass
        # self.temp = 20

    def get_temp(self):
        return 20

    def get_humid(self):
        return 10

    def _callback(self, callback, *args):
        if callback:
            try:
                callback(self, *args)
            except Exception as e:
                _logging.error("error from callback {}: {}".format(callback, e))
                if _logging.isEnabledForDebug():
                    _, _, tb = sys.exc_info()
                    traceback.print_tb(tb)


if __name__ == 'main':
    pass
