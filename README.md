
# BU EC601 mini project 3

This mini project contains two database implementations with MySQL and MongoDB.
# Create MYSQL database
Use the following code to create database and table, then insert information into table:

    dbb = pymysql.connect(host = "localhost", user = "root", passwd = "!", db ="ec601mini3")
    cursor = dbb.cursor()
    sql = """CREATE TABLE mini3_database (
             username CHAR(45) NOT NULL,
             twtnum INT NOT NULL,
             picnum INT NOT NULL,
             timei CHAR(50) NOT NULL,
             picaddress CHAR(100) NOT NULL,
             tags CHAR(200) NOT NULL)"""
    print('Table created successfully!')
