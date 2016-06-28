#!/usr/bin/env python
# -*- coding: utf-8 -*-
import html2text
import xml.etree.ElementTree as ET

def convert(args):
    tree = ET.parse(args.filename)
    root = tree.getroot()

    title = root.find('title').text
    content = root.find('content').text

    # Verify that there is a chapo
    chapo = root.find('chapo')
    if chapo is not None:
        chapo = chapo.text
        content = chapo + content


    print('Converted markdown :')
    print(html2text.html2text(content))
