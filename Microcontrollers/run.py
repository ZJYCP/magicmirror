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
from utils.db.dbContr import MirrorMysql
from utils.websocket.ws import WebSocketServer


def _init():
    global th, db,ws_server,scheduler

    # 实例化温湿度传感器对象
    th = TempHumid()

    # 实例化数据库对象
    db = MirrorMysql(host="127.0.0.1",
                     port=3306,
                     user="root",
                     passwd="root",
                     db="magicMirror",
                     charset="utf8mb4")

    # 创建websocket服务
    ws_server = WebSocketServer()

    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()


def temp_humid_task():
    temp = th.get_temp()
    humid = th.get_humid()
    logger.debug('温度:%s,湿度:%s' % (temp, humid))
    # TODO 数据有变化才进行数据库写入
    db.insertsqlone(tablename="temp_humid", temp=temp, humid=humid)


def run():

    # 添加温湿度监测调度任务
    scheduler.add_job(temp_humid_task, 'interval', seconds=5)
    # 启动调度任务
    scheduler.start()

    ws_server.begin()


if __name__ == '__main__':
    _init()
    run()
    while 1:
        pass
