#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import pymongo
import datetime

# Write information into the mini3_database database.
def mysql(twnum,picnum,picaddress,newtag):
    # Connect to the database.
    dbb = pymysql.connect(host = "localhost", user = "root", passwd = "", db ="ec601mini3")
    cursor = dbb.cursor()
    times = datetime.datetime.now()
    print(times)
    # Insert
    sql = "INSERT INTO mini3_database(username, \
           twtnum,picnum,timei, picaddress, tags) \
           VALUES ('%s', %s, %s, '%s', '%s','%s')" % \
          ('Username', twnum, picnum, times, picaddress,newtag)

    try:
       cursor.execute(sql)
       dbb.commit()
       print('Data inserted successfully!')
    except:
       # Rollback in case there is any error
       dbb.rollback()
       print("Can't connect to mysql database!")

    dbb.close()

# Create table
def create():
    dbb = pymysql.connect(host = "localhost", user = "root", passwd = "", db ="ec601mini3")
    cursor = dbb.cursor()
    cursor.execute("DROP TABLE IF EXISTS mini3_database")

    # Create table
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
    mysql('twtnum', 'picnum', 'picaddress', 'newtag')


