#! /bin/env python
# -*-coding:utf8-*-


'''
Autrhor:yushuai
Date:2018-03-07
Func:自动发送邮件的
'''
import sys

import xml.etree.ElementTree as Et


class XmlParser:

    def __init__(self, xml_file):
        self.title = ""
        self.mailTo = ""
        self.queryTitle = ""
        self.sql = []
        self.root = Et.ElementTree(file=xml_file).getroot()

        for i in self.root:
            if i.tag == "mail-to":
                self.mail_to = i.text
            elif i.tag == "title":
                self.title = i.text
            elif i.tag == "content":
                for j in i:
                    if j.tag == "report":
                        self.sql.append(j[1].text)

    def getMailTo(self):
        return self.mailTo

    def getTitle(self):
        return self.title

    def getSql(self):
        return self.sql


def help():
    help_str = "mailReport.py xxx.xml\n"
    print(help_str)


if __name__ == '__main__':
    xml_file = sys.argv[1]

    # 1.解析XML文件

    # 2.生成邮件信息

    # 3.发送信息
