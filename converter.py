#!/usr/bin/env python
# -*- coding: utf-8 -*-
import html2text
import xml.etree.ElementTree as ET

def convert(args):
    print('First test converting HTML to MD:')
    print(html2text.html2text("<p><strong>Zed's</strong> dead baby, <em>Zed's</em> dead.</p>"))

    print('Got this file:')
    print(args.filename)

    print('File converted :')

    tree = ET.parse(args.filename)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)
