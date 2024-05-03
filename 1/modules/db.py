#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import sqlite3
import os
from threading import Lock
############static variables#####################

#################################################


class DB:
    def __init__(self, path):
        super(DB, self).__init__()
        self.__lock = Lock()
        self.__db_path = path
        self.__cursor = None
        self.__db = None
        self.init()

    def init(self):
        if not os.path.exists(self.__db_path):
            self.__db = sqlite3.connect(self.__db_path, check_same_thread=False)
            self.__cursor = self.__db.cursor()
            self.__cursor.execute('''
            CREATE TABLE users(
            row_id INTEGER primary key autoincrement not null,
            name TEXT,
            lastname TEXT,
            email TEXT,
            login TEXT,
            password TEXT
            )
            ''')
            self.__cursor.execute('''
            CREATE TABLE appartaments(
            row_id INTEGER primary key autoincrement not null,
            link TEXT,
            address TEXT,
            floor TEXT,
            square TEXT,
            rooms TEXT,
            price TEXT,
            date TEXT,
            source TEXT,
            comments TEXT
            )
            ''')
            self.__db.commit()
        else:
            self.__db = sqlite3.connect(self.__db_path, check_same_thread=False)
            self.__cursor = self.__db.cursor()

    def db_write(self, queri, args):
        with self.__lock:
            self.__cursor.execute(queri, args)
            self.__db.commit()

    def db_read(self, queri, args):
        with self.__lock:
            self.__cursor.execute(queri, args)
            return self.__cursor.fetchall()