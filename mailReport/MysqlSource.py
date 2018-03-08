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

    def select(self, sql):
        try:
            self._cur.execute(sql)
            data = self._cur.fetchall()
            return data

        except Exception as e:
            if self._cur:
                self._cur.close()

            self._conn.close()
        return None

    def close(self):
        if self._cur:
            self._cur.close()

        self._conn.close()


if __name__ == "__main__":
    aaa = MysqlSource("10.37.15.18", "bi_ys", "ak3c3dsi349zdk", db="daojia_dwh", port=3306)
    for i in aaa.select("select * from information_schema.tables limit 100"):
        print(i)
    print('\n' * 4)
    for i in aaa.select("select * from information_schema.VIEWS limit 100"):
        print(i)
