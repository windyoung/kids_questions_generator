# coding=utf-8
#!/usr/bin/env python3
import os
import sqlite3
import sys
# sys.path.append('..\\数学加减法')
sys.path.append('.\\')
from 数学加减法.Mathematical_formula_exhaustor import *


class DB_file_generator():
    def __init__(self) -> None:
        pass

    def create_local_db(self, datafile: str) -> sqlite3.Connection:
        "创建或连接数据库 文件数据库"
        # datafile = r"./data/db/test_sqlite.db"
        if os.path.exists(datafile):
            self.db = sqlite3.connect(datafile)
            print(datafile, " connected")
        else:
            path_ = os.path.split(datafile)[0]
            if os.path.exists(path_):
                pass
            else:
                os.mkdir(path_)
            self.db = sqlite3.connect(datafile)
            print(datafile, "created")
        return self.db

    def commit_db_transaction(self, db_conn: sqlite3.Connection):
        db_conn.commit()

    def rollback_db_transaction(self, db_conn: sqlite3.Connection):
        db_conn.rollback()

    def destory_db_connection(self, db_conn: sqlite3.Connection):
        db_conn.close()
        pass

    def check_table_exists(self, db_conn: sqlite3.Connection, tbl_name: str):
        "检查表是否存在"
        cur = db_conn.cursor()
        check_sql = """SELECT tbl_name FROM sqlite_master WHERE type='table' AND tbl_name='{}'; """.format(
            tbl_name)
        listOfTables = cur.execute(check_sql).fetchall()
        if listOfTables == []:
            return {"res": False, "str": "Table {} not exists".format(tbl_name)}
        else:
            return {"res": True, "str": "Table {} exists".format(tbl_name)}

    def create_db_table(self, db_conn: sqlite3.Connection, table_info: dict) -> bool:
        "创建表"
        tbl_name = table_info["name"]
        tbl_data = table_info["datalist"]
        res_t = self.check_table_exists(db_conn, tbl_name)
        if res_t["res"] == True:
            print('Table exists!')
        else:
            # 获取 表的及列表的列大小
            keys_ = {}
            for one_record in tbl_data:
                for key in one_record:
                    if key not in keys_:
                        keys_[key] = 0
                    len_ = len(str(one_record[key]))
                    if len_ > keys_[key]:
                        keys_[key] = len_
            print(keys_)
            # 组件 建表语句
            for key in keys_:
                sql_column ="{} char({}) not null,".format(keys_)
            sql_creat_table = """ create table {0}
            (id int primary key not null,
            {1} 
            comment char(30) );
            """.format(tbl_name,sql_column)
            print(sql_creat_table)


if __name__ == '__main__':

    # 表信息
    a = Mathematical_formula_exhaustor()
    res_tbl = a.plus_under_10(0)

    # 创建数据文件
    datafile = r"./data/db/test_1.db"
    b = DB_file_generator()
    b_db_conn = b.create_local_db(datafile)
    b.create_db_table(b_db_conn, res_tbl)
