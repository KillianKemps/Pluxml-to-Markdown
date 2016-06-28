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
    content = root.find('content')

    # Declare array here in case content in None
    local_images_src = []

    # Get content if there is one
    if content is not None:
        content = content.text

        if content is not None:
            # Parse images
            html = BeautifulSoup(content, 'html.parser')
            local_images = html.find_all(src=re.compile('^data/images'))

            local_images_src = [image.get('src') for image in local_images]

            # Convert the HTML content to Markdown
            content = html2text.html2text(content)
        else:
            content = ''

    # Get chapo is there is one
    chapo = root.find('chapo')
    if chapo is not None:
        chapo = chapo.text

        if chapo is not None:
            chapo = html2text.html2text(chapo)
        else:
            chapo = ''

    # Get the date from the file name
    date = post.name.split('.')[-3]
    formatted_date = datetime.strptime(date, "%Y%m%d%H%M")
    formatted_date = formatted_date.strftime("%d-%m-%Y %H:%M")

    # Check if the post is a draft in its filename
    draft = re.search( 'draft', post.name)
    if draft is not None:
        draft = True
    else:
        draft = False

    print(bcolors.OKBLUE + 'Parsing finished' + bcolors.ENDC)

    return {
        'filename': post.name,
        'title': title,
        'draft': draft,
        'date': formatted_date,
        'tags': tags,
        'chapo': chapo,
        'content': content,
        'images': local_images_src}
