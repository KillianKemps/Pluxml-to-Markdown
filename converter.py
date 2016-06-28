#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def toGrav(post):
    # Write YAML header for Markdown file
    header = '---'
    header += '\n' + 'title: ' + post['title']
    if post['tags'] is not None:
        header += '\n' + 'tag: ' + post['tags']
    header += '\n' + 'date: ' + str(post['date'])
    header += '\n' + '---' + '\n'

    print('Converted markdown :')
    print(header)
    # print(post['content'])

    # Create target folder if it doesn't exist
    folder_name = 'converted_posts'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_basename = os.path.basename(post['filename'])
    target_filename = os.path.splitext(file_basename)[0] + '.md'

    target_file = open(folder_name + '/' + target_filename, 'w')
    target_file.write(header + post['chapo'] + post['content'])
    target_file.close()
