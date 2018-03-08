#! /bin/env python
# -*-coding:utf8-*-

"""
解析XML，按照规定格式返回数据

"""

import xml.etree.ElementTree as Et


class XmlParser:

    def __init__(self, xml_file):

        self.report = []
        self.root = Et.parse(xml_file).getroot()

        for node in self.root:
            if node.tag == "mail-to":
                self.mail_to = node.text.strip()

            elif node.tag == "subject":
                self.subject = node.text.strip()

            elif node.tag == "mail-cc":
                self.mail_cc = node.text.strip()

            elif node.tag == "report":
                res = {}
                for sub_node in node:
                    if sub_node.tag == "title":
                        res["title"] = sub_node.text.strip()
                    if sub_node.tag == "sql":
                        res["sql"] = sub_node.text.strip()
                    if sub_node.tag == "text":
                        res["text"] = sub_node.text.strip()
                self.report.append(res)

    def get_mail_to(self):
        return self.mail_to

    def get_mail_cc(self):
        return self.mail_cc

    def get_subject(self):
        return self.subject

    def get_report(self):
        return self.report


if __name__ == '__main__':
    xml_file = 'D:\\tmp.xml'

    aaa = XmlParser(xml_file)

    print(aaa.get_mail_to() + '\n')
    print(aaa.get_mail_cc() + '\n')
    print(aaa.get_subject() + '\n')
    print(aaa.get_report())
