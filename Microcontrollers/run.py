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
from utils.websocket.ws import WebSocketServer

import requests
import json

import models.Infrared as remoteSen

import sys
from twisted.internet import reactor
from twisted.python import log
from utils.pusher_client import PusherClient
import threading


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter


    def run(self):
        print ("开始线程：" + self.name)
        _init()
        run()
        try:
            # 模拟主进程持续运行
            while True:
                time.sleep(2)
        except(KeyboardInterrupt, SystemExit):
            # Not strictly necessary if daemonic mode is enabled but should be done if possible
            scheduler.shutdown()
            print('Exit The Job!')
        print ("退出线程：" + self.name)

def _init():
    global th, db, ws_server, scheduler

    # 实例化温湿度传感器对象
    th = TempHumid()

    # 实例化数据库对象
    # db = MirrorMysql(host="127.0.0.1",
    #                  port=3306,
    #                  user="root",
    #                  passwd="root",
    #                  db="magicMirror",
    #                  charset="utf8mb4")

    # 创建websocket服务
    # ws_server = WebSocketServer()

    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()


def temp_humid_task():
    temp = th.get_temp()
    humid = th.get_humid()

    url = "http://mirror.com/api/micro/temp"
    formdata = {
        'temp': 11,
        'humid': 22,
        'sound': 33
    }
    if th.is_same(temp, humid):
        response = requests.post(url, data=formdata)
        if response.json()['code']==200:
            logger.debug('温度:%s,湿度:%s 添加成功' % (temp, humid))
        # db.insertsqlone(tablename="temp_humid", temp=temp, humid=humid)


def run():
    # 传感器
    remoteSen.start()

    # 添加温湿度监测调度任务
    scheduler.add_job(temp_humid_task, 'interval', seconds=5)
    # 启动调度任务
    scheduler.start()

    # 启动websocket服务
    # ws_server.begin()


def run_pusher(event, data):
    def on_data(channel, event, data):
        print(data)
    channel = bitstamp.subscribe("alarm")
    channel.bind("App\\Events\\PushAlarmEvent", on_data)


if __name__ == '__main__':

    thread1 = myThread(1, "Thread-1", 1)
    thread1.start()

    bitstamp = PusherClient("6a9ab7f96acaf8cbb06f")

    bitstamp.on("pusher:connection_established", run_pusher)

    log.startLogging(sys.stdout)
    reactor.run()





