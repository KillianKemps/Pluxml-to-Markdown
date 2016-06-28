#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, date, time
import html2text
import xml.etree.ElementTree as ET

def parser(post):
    """
    Parse PluXML post in order to be converted afterwards
    """
    tree = ET.parse(post)
    root = tree.getroot()

    title = root.find('title').text
    tags = root.find('tags').text
    content = root.find('content').text

    # Get the date from the file name
    date = post.name.split('.')[-3]
    formatted_date = datetime.strptime(date, "%Y%m%d%H%M")

    # Verify that there is a chapo
    chapo = root.find('chapo')
    if chapo is not None:
        chapo = chapo.text
        content = chapo + content

    # Convert the HTML content to Markdown
    converted_content = html2text.html2text(content)

    return {
        'filename': post.name,
        'title': title,
        'date': formatted_date,
        'tags': tags,
        'chapo': chapo,
        'content': converted_content}
