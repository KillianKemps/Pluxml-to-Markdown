#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import re

from utils import bcolors


def toSimpleMarkdown(post, folder):
    """
    Convert to Markdown (without headers)
    """
    # Create output folder if it doesn't exist
    folder_name = 'converted_posts'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Set filename
    file_basename = os.path.basename(post['filename'])
    target_filename = os.path.splitext(file_basename)[0] + '.md'

    # Write converted file
    with open(folder_name + '/' + target_filename, 'w') as target_file:
        target_file.write(post['chapo'] + post['content'])


def toGrav(post, folder):
    """
    Convert to Markdown + YAML Front Matter for Grav CMS
    """
    # Escape double quotes from title
    if re.search('"', post['title']):
        post['title'] = '\'' + post['title'] + '\''

    # Write YAML header for Markdown file
    header = '---'
    header += '\n' + 'title: ' + post['title']
    if post['tags'] is not None:
        header += '\n' + 'tag: ' + post['tags']
    if post['draft'] is True:
        header += '\n' + 'published: false '
    header += '\n' + 'date: \'' + str(post['date'] +'\'')
    header += '\n' + '---' + '\n'

    # As html2text library currently inserts newlines when links are too long,
    # it is currently needed to fix them here
    # See: https://github.com/Alir3z4/html2text/issues/127
    def remove_newlines(match):
        print('matched: ', match.group())
        print('Gonna return :',"".join(match.group().strip().split('\n')))
        return "".join(match.group().strip().split('\n'))

    links_pattern = re.compile(r'\[([\w\s*:/\-\.]*)\]\(([^()]+)\)')
    post['content'] = links_pattern.sub(remove_newlines, post['content'])

    # Change all PluXML images sources by local one (images will be copied
    # afterwards)
    if len(post['images']) is not 0:
        src = re.compile(r'!\[([\w\s*:/\-\.]*)\]\(data\/images\/')
        post['content'] = src.sub(r'![\1](', post['content'])

    # Create summary if there is a chapo
    if post['chapo'] is not '':
        post['chapo'] += '===\n\n'

    print('Converted markdown :')
    print(header)

    # Create output folder if it doesn't exist yet
    folder_name = 'converted_posts'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Create unique folder for the post
    post_folder = post['filename'].split('.')[-2]
    post_folder_path = folder_name + '/' + post_folder
    if not os.path.exists(post_folder_path):
        os.makedirs(post_folder_path)

    # Set item.md as filename which is ideal for a Grav blog
    target_filename = 'item.md'

    # Write converted file
    with open(post_folder_path + '/' + target_filename, 'w') as target_file:
        target_file.write(header + post['chapo'] + post['content'])

    # If they are images, copy them from PluXml folder into the new folder
    for image in post['images']:
        print('Copying image from: ', folder + '/images/' +
              os.path.basename(image))
        image_path = folder + '/images/' + os.path.basename(image)
        try:
            shutil.copy2(image_path, post_folder_path)
        except FileNotFoundError:
            print(bcolors.FAIL + 'Error: Image {0} doesn\'t seem to exist and \
                  has not been copied'.format(image) + bcolors.ENDC)
