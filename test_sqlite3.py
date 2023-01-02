# coding=utf-8
#!/usr/bin/env python3
import sqlite3
import os


def create_local_db():
    "创建或连接数据库 文件数据库"
    datafile = r"./data/db/test_sqlite.db"
    if os.path.exists(datafile):
        db = sqlite3.connect(datafile)
    print(datafile, "created/connected")
    return db


def create_mem_db():
    "创建或连接数据库 内存数据库"
    datafile_mem = r":memory:"
    # db = sqlite3.connect("file::memory:?cache=shared")
    db = sqlite3.connect(datafile_mem)
    print(datafile_mem, "created/connected")
    return db


def check_table(db_conn: sqlite3.Connection):
    "检查表是否存在"
    cur=db_conn.cursor()
    # sqlite_master https://www.cnblogs.com/Mz1-rc/p/15380735.html
    check_sql="""SELECT tbl_name FROM sqlite_master WHERE type='table' AND tbl_name='company'; """
    listOfTables = cur.execute(check_sql).fetchall()
    return listOfTables
    

def create_table(db_conn:sqlite3.Connection):
    "创建表"
    cur=db_conn.cursor()
    # 检测表是否存在
    listOfTables=check_table(db_conn)
    if listOfTables == []:
        print('Table not found!')
        # 创建表
        sql_creat_table=""" create table company
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real);
        """
        cur.execute(sql_creat_table)
        db_conn.commit()
        print("建表成功")
    else:
        print('Table found!')
    # db_conn.close()
    
    
def insert_data(db_conn:sqlite3.Connection):
    cur=db_conn.cursor()
    sql1="""insert into company (id , name , age , address , salary)  values (3 , '王五' , 32 , '天堂' , 5555);"""
    sql2="""insert into company (id , name , age , address , salary) values (2 , '李四' , 62 , '城南' , 15615);"""
    cur.execute(sql1)
    cur.execute(sql2)
    db_conn.commit()
    db_conn.close()
    pass


def select_data(db_conn: sqlite3.Connection):
    "查询数据"
    cur=db_conn.cursor()
    sql = '''select * from company;'''
    cur.execute(sql)
    for row in cur:
        print(row)
    print("查询完成")
    

if __name__ == '__main__':
    pass
    db=create_local_db()
    # create_table(db)
    # insert_data(db)
    select_data(db)