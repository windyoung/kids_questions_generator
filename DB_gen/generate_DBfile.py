# coding=utf-8
#!/usr/bin/env python3
import sqlite3
import os


class DB_file_generator():
    def __init__(self) -> None:
        pass
    def create_local_db(self,datafile: str)->sqlite3.Connection:
        "创建或连接数据库 文件数据库"
        # datafile = r"./data/db/test_sqlite.db"
        if os.path.exists(datafile):
            db = sqlite3.connect(datafile)
        print(datafile, "created/connected")
        return db
