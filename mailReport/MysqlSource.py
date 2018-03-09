#! /bin/env python
# -*-coding:utf8-*-

"""
链接Mysql查询数据
"""

import pymysql


class MysqlSource(object):
    def __init__(self, host=None, user=None, passwd=None, db=None, port=3306):

        assert host
        assert user
        assert passwd
        assert db
        assert type(port) is int

        self._conn = pymysql.connect(host=host, user=user, password=passwd, db=db, port=port)
        self._cur = self._conn.cursor()
        self._data = None
        self._desc = None

    def select(self, sql):
        try:
            self._cur.execute(sql)
            self._data = self._cur.fetchall()
            self._desc = self._cur.description

            return self._data

        except Exception as e:
            if self._cur:
                self._cur.close()

            self._conn.close()
        return None

    def get_desc(self):
        res = []
        for column in self._desc:
            res.append(column[0].strip())
        return res

    def close(self):
        if self._cur:
            self._cur.close()

        self._conn.close()



