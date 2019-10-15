#!/usr/bin/env python
# encoding: utf-8
"""
@author: Glyn
@contact: chnzjycp@foxmail.com
@file: run.py
@time: 19-8-5 下午12:54
@desc: 主程序
"""

import datetime
import time
from utils.logger import *
from models.TempHumid import TempHumid
from apscheduler.schedulers.background import BackgroundScheduler
# from utils.db.dbContr import MirrorMysql
# from utils.websocket.ws import WebSocketServer

import requests
import json

import models.Infrared as remoteSen

# pusher、多进程
import sys
from twisted.internet import reactor
from twisted.python import log
from utils.pusher_client import PusherClient
from multiprocessing import Process


def _init():
    global th,scheduler

    # 实例化温湿度传感器对象
    th = TempHumid()

    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()
    # 传感器
    remoteSen.start()

    # 添加温湿度监测调度任务
    scheduler.add_job(temp_humid_task, 'interval', seconds=5)
    # 启动调度任务
    scheduler.start()

    try:
        # 模拟主进程持续运行
        while True:
            time.sleep(2)
    except(KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')


def temp_humid_task():
    temp = th.get_temp()
    humid = th.get_humid()

    print('temp_task')
    url = "http://mirror.com/api/micro/temp"
    formdata = {
        'temp': 11,
        'humid': 22,
        'sound': 33
    }

    if th.is_same(temp, humid):
        response = requests.post(url, data=formdata)
        if response.json()['code'] == 200:
            logger.debug('温度:%s,湿度:%s 添加成功' % (temp, humid))


def run_pusher(event, data):
    def on_data(channel, event, data):
        print(data)

    channel = bitstamp.subscribe("alarm")
    channel.bind("App\\Events\\PushAlarmEvent", on_data)


if __name__ == '__main__':
    p = Process(target=_init, args=())
    print('Child process will start.')
    p.start()

    bitstamp = PusherClient("6a9ab7f96acaf8cbb06f")

    bitstamp.on("pusher:connection_established", run_pusher)

    log.startLogging(sys.stdout)
    reactor.run()
