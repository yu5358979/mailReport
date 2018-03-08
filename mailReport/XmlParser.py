#! /bin/env python
# -*-coding:utf8-*-

"""
解析XML，按照规定格式返回数据

"""

import xml.etree.ElementTree as Et


class XmlParser(object):

    def __init__(self, xml_file):

        self._report = []
        self._root = Et.parse(xml_file).getroot()

        for node in self._root:
            if node.tag == "mail-to":
                self._mail_to = node.text.strip()

            elif node.tag == "subject":
                self._subject = node.text.strip()

            elif node.tag == "mail-cc":
                self._mail_cc = node.text.strip()

            elif node.tag == "report":
                res = {}
                for sub_node in node:
                    if sub_node.tag == "title":
                        res["title"] = sub_node.text.strip()
                    if sub_node.tag == "sql":
                        res["sql"] = sub_node.text.strip()
                    if sub_node.tag == "text":
                        res["text"] = sub_node.text.strip()
                self._report.append(res)

    def get_mail_to(self):
        return self._mail_to

    def get_mail_cc(self):
        return self._mail_cc

    def get_subject(self):
        return self._subject

    def get_report(self):
        return self._report


if __name__ == '__main__':
    xml_file = 'D:\\tmp.xml'

    aaa = XmlParser(xml_file)

    print(aaa.get_mail_to() + '\n')
    print(aaa.get_mail_cc() + '\n')
    print(aaa.get_subject() + '\n')
    print(aaa.get_report())

    aaa.get_mail_cc
