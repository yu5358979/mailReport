#! /bin/env python
# -*-coding:utf8-*-

import xml.etree.ElementTree as ET

root = ET.parse('D:\\tmp.xml').getroot()

print(root.tag, root.attrib)

for i in root:
    if i.tag != "report":
        print(i.tag, i.attrib, i.text)
    else:
        for j in i:
            print(j.tag, j.attrib, j.text)
