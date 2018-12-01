#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import pymongo
import datetime

# Write information into the mini3_database database.
def mysql(twnum,picnum,picaddress,newtag):
    # 打开数据库连接Connect to the database.
    dbb = pymysql.connect(host = "localhost", user = "root", passwd = "FORever23mm!", db ="ec601mini3")
    # 使用cursor()方法获取操作游标
    cursor = dbb.cursor()
    times = datetime.datetime.now()
    print(times)
    # SQL 插入语句 Insert
    sql = "INSERT INTO mini3_database(username, \
           twtnum,picnum,timei, picaddress, tags) \
           VALUES ('%s', %s, %s, '%s', '%s','%s')" % \
          ('Username', twnum, picnum, times, picaddress,newtag)
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       dbb.commit()
       print('Data inserted successfully!')
    except:
       # Rollback in case there is any error
       # 发生错误时回滚
       dbb.rollback()
       print("Can't connect to mysql database!")

    # 关闭数据库连接
    dbb.close()

# Create table
def create():
    dbb = pymysql.connect(host = "localhost", user = "root", passwd = "FORever23mm!", db ="ec601mini3")
    # 使用cursor()方法获取操作游标
    cursor = dbb.cursor()

    # 如果数据表已经存在使用 execute() 方法删除表。
    cursor.execute("DROP TABLE IF EXISTS mini3_database")

    # 创建数据表SQL语句
    sql = """CREATE TABLE mini3_database (
             username CHAR(45) NOT NULL,
             twtnum INT NOT NULL,
             picnum INT NOT NULL,
             timei CHAR(50) NOT NULL,
             picaddress CHAR(100) NOT NULL,
             tags CHAR(200) NOT NULL)"""
    print('Table created successfully!')
    cursor.execute(sql)
    cursor.close()
    dbb.close()




if __name__ == '__main__':
    create()
    mysql('twnum', 'picnum', 'picaddress', 'newtag')


