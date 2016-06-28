#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from datetime import datetime, date, time
import xml.etree.ElementTree as ET

import html2text
from bs4 import BeautifulSoup

from utils import bcolors


def parser(post):
    """
    Parse PluXML post in order to be converted afterwards
    """
    tree = ET.parse(post)
    root = tree.getroot()

    title = root.find('title').text

    print('\n' + '*'*80)
    print(bcolors.OKBLUE + 'Parsing {0} post'.format(title) + bcolors.ENDC)

    tags = root.find('tags').text
    content = root.find('content').text

    # Get the date from the file name
    date = post.name.split('.')[-3]
    formatted_date = datetime.strptime(date, "%Y%m%d%H%M")

    # Verify that there is a chapo
    chapo = root.find('chapo')
    if chapo is not None:
        chapo = chapo.text
        chapo = html2text.html2text(chapo)

    # Convert the HTML content to Markdown
    converted_content = html2text.html2text(content)

    # Parse images
    html = BeautifulSoup(content, 'html.parser')
    local_images = html.find_all(src=re.compile('^data/images'))

    local_images_src = [image.get('src') for image in local_images]

    print(bcolors.OKBLUE + 'Parsing finished' + bcolors.ENDC)

    return {
        'filename': post.name,
        'title': title,
        'date': formatted_date,
        'tags': tags,
        'chapo': chapo,
        'content': converted_content,
        'images': local_images_src}
