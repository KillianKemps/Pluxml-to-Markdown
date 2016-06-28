#!/usr/bin/env python
# -*- coding: utf-8 -*-
import html2text
import xml.etree.ElementTree as ET

def convert(args):
    tree = ET.parse(args.filename)
    root = tree.getroot()

    title = root.find('title').text
    chapo = root.find('chapo').text
    content = root.find('content').text

    print('Converted markdown :')
    print(html2text.html2text(chapo + content))
