#!/usr/bin/env python
# encoding: utf-8
"""
@author: Glyn
@contact: chnzjycp@foxmail.com
@file: dbContr.py
@time: 19-8-5 下午2:48
@desc:数据库封装
"""

import pymysql

"""
说明:
1.maketable()  格式 : tablename(表名),**field(key='字段名',value='字段说明')  默认的字段类型为varchar(255)
2.insertsqlone()  格式 : tablename,**field(key='字段名',value='字段值')  **field长度不限
3.querysql()  格式 : *Choicefield(表名=列表第一个值+查询的字段。),**kwargs(条件例如 id='1314' 长度限为“1”)
4.updateone() 格式 : *kw(表名=列表第一个值+字段+字段需要更新的值),**field(查询条件 比如id='1')
5.deleteone() 格式 : tablename,**field(查询条件 比如 id=1)
"""


class MirrorMysql(object):

    def __init__(self, host, port, user, passwd, db, charset):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        try:
            self.condb = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                         passwd=self.passwd, db=self.db, charset=self.charset)
        except Exception as abnormal:
            print("数据库连接错误，错误内容%s " % abnormal)
        # 创建一个游标对象
        self.cursor = self.condb.cursor()

    # 创建数据表
    def maketable(self, tablename, **field):
        basesql = ""  # 定义basesql
        num = self.cursor.execute("DROP TABLE IF EXISTS %s" % tablename)       # 判断表名为tablename表名是否存在，如果是 直接删除

        # 将field，拼接basesql
        for key in field:
            basesql = basesql + "%s varchar(255) DEFAULT NULL COMMENT '%s'," % (key, field.get(key))

        makesql = """
        CREATE TABLE %s (
        id int(11) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
            %s
            PRIMARY KEY (`id`)
        )
        """ % (tablename, basesql)
        # 执行建表SQL
        num = self.cursor.execute(makesql)
        print("表:'%s' 创建成功" % tablename)

    def insertsqlone(self, tablename, **field):

        i = 0
        liststr = listfield = ""  # 字段的集合
        listvalues = []  # values字段对应值的集合
        for key in field:
            liststr = liststr + "%s," % key
            listvalues.append(field[key])
            i = i + 1
        listfield = "(" + liststr[0:len(liststr) - 1] + ")"  # 最终的字段集合
        values = tuple(listvalues)  # 最终的字段值集合

        # sql语句
        insertsql = "INSERT INTO %s%s VALUES %s" % (tablename, listfield, values)
        try:
            self.cursor.execute(insertsql)  # 执行SQL
            self.condb.commit()  # 提交到数据库执行
        except Exception as  abnormal:
            self.condb.rollback()  # 发生错误的时候 回滚
            print("执行失败 insert语句:'%s'，失败信息为 %s" % (insertsql, abnormal))
        # 判断是否执行成功
        if self.cursor.rowcount == 1:
            print("执行成功 insert语句:'%s'" % insertsql)

    def querysql(self, *Choicefield, **kwargs):
        tablename = list(Choicefield)[0]  # 取第一个参数，作为表名
        fieldstr = ""  # 定义一个fieldstr用于拼接中转

        # 将输入的Choicefield列表转化成查询格式
        for i in range(1, len(list(Choicefield))):
            fieldstr = fieldstr + list(Choicefield)[i] + ","
        field = fieldstr[0:len(fieldstr) - 1]  # 将拼接之后的str 去掉最后的","
        # 判断输入**kwargs的键值对数量
        if len(kwargs) != 1:
            print("SQL查询条件暂时只支持一个")
        else:
            for key in kwargs:
                sqlquery = "select %s from %s where %s='%s'" % (field, tablename, key, kwargs[key])
                break
            try:
                num = self.cursor.execute(sqlquery)  # 影响的行数
            except Exception as  abnormal:
                print("SQL有误，错误内容 %s" % abnormal)

            if num == 0:  # 0 则代表没有查询结果
                return "没有查询的结果.."
            elif num == 1:  # 影响行数 为1 fetchone
                return list(self.cursor.fetchone())
            else:  # 多行情况下 使用fetchall
                return list(self.cursor.fetchall())

    def updateone(self, *kw, **field):
        if len(field) != 1:
            raise Exception("条件过长，只允许输入一个条件")
            exit()
        for key in field:
            updatesql = "UPDATE %s SET  %s = '%s' WHERE %s = '%s'" % (kw[0], kw[1], kw[2], key, field.get(key))
        try:
            self.cursor.execute(updatesql)
            self.condb.commit()
        except Exception as abnormal:
            self.condb.rollback()
            print("执行失败!update语句:'%s', 失败内容为 %s" % (updatesql, abnormal))
            exit()
        # 判断是否更新成功
        if self.cursor.rowcount == 1:
            print("执行成功!update语句:'%s'" % updatesql)
        else:
            print("执行成功!update语句:'%s'，warning:更新后的值与跟新之前的值相等，或者查询不到对应的结果" % updatesql)

    def deleteone(self, tablename, **field):
        if len(field) != 1:
            raise Exception("条件过长，只允许输入一个条件")
            exit()
        for key in field:
            deletesql = "delete from %s  WHERE %s = '%s'" % (tablename, key, field.get(key))
        try:
            self.cursor.execute(deletesql)
            self.condb.commit()
        except Exception as abnormal:
            self.condb.rollback()
            print("执行失败!delete语句:'%s', 失败内容为 %s" % (deletesql, abnormal))
            exit()
        # 判断是否更新成功
        if self.cursor.rowcount == 1:
            print("执行成功!delete语句:'%s'" % deletesql)

    # 析构函数
    def __del__(self):
        self.cursor.close()
        self.condb.close()


if __name__ == '__main__':
    pass
    # 实例化
    # diycon = MirrorMysql(host="127.0.0.1", port=3306, user="root",
    #                      passwd="root", db="magicMirror", charset="utf8mb4")

    # 1.新建一个名称为 tb_xiejiangpeng的表，字段为name,age,address,其中的value为字段说明
    # diycon.maketable(tablename="tb_xiejiangpeng", name="姓名", age="年龄", address="家庭住址")

    # 2.在tb_xiejiangpeng表中 插入一条数据
    # diycon.insertsqlone(tablename="temp_humid", temp=10.2, humid=33.33)

    # 3.根据name=谢江鹏 查询刚才插入的数据
    # queryresult = diycon.querysql("tb_xiejiangpeng", "*", name="谢江鹏")
    # print("查询到的结果为:", queryresult)

    # 4.将id=1的那条数据 名称修改成"彭敏"
    # diycon.updateone("tb_xiejiangpeng", "name", "彭敏", id="1")

    # 5.删除name='彭敏'的那条数据
    # diycon.deleteone("tb_xiejiangpeng", name="彭敏")
