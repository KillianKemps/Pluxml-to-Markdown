#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime, date, time
import html2text
import xml.etree.ElementTree as ET

def convert(args):
    tree = ET.parse(args.post)
    root = tree.getroot()

    title = root.find('title').text
    tags = root.find('tags').text
    content = root.find('content').text

    # Get the date from the file name
    date = args.post.name.split('.')[-3]
    formatted_date = datetime.strptime(date, "%Y%m%d%H%M")

    # Verify that there is a chapo
    chapo = root.find('chapo')
    if chapo is not None:
        chapo = chapo.text
        content = chapo + content

    # Convert the HTML content to Markdown
    converted_content = html2text.html2text(content)

    # Write YAML header for Markdown file
    header = '---'
    header += '\n' + 'title: ' + title
    if tags is not None:
        header += '\n' + 'tag: ' + tags
    header += '\n' + 'date: ' + str(formatted_date)
    header += '\n' + '---' + '\n'

    print('Converted markdown :')
    print(header)
    print(converted_content)

    # Create target folder if it doesn't exist
    folder_name = 'converted_posts'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_basename = os.path.basename(args.post.name)
    target_filename = os.path.splitext(file_basename)[0] + '.md'

    target_file = open(folder_name + '/' +target_filename, 'w')
    target_file.write(header + converted_content)
    target_file.close()
