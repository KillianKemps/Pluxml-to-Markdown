#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil

from utils import bcolors


def toSimpleMarkdown(post, folder):
    """
    Convert to Markdown (without headers)
    """
    # Create output folder if it doesn't exist
    folder_name = 'converted_posts'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_basename = os.path.basename(post['filename'])
    target_filename = os.path.splitext(file_basename)[0] + '.md'

    target_file = open(folder_name + '/' + target_filename, 'w')
    target_file.write(header + post['chapo'] + post['content'])
    target_file.close()


def toGrav(post, folder):
    """
    Convert to Markdown + YAML Front Matter for Grav CMS
    """
    # Write YAML header for Markdown file
    header = '---'
    header += '\n' + 'title: ' + post['title']
    if post['tags'] is not None:
        header += '\n' + 'tag: ' + post['tags']
    if post['draft'] is True:
        header += '\n' + 'published: false '
    header += '\n' + 'date: ' + str(post['date'])
    header += '\n' + '---' + '\n'

    print('Converted markdown :')
    print(header)

    # Create output folder if it doesn't exist
    folder_name = 'converted_posts'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Create folder for post
    post_folder = post['filename'].split('.')[-2]
    post_folder_path = folder_name + '/' + post_folder
    if not os.path.exists(post_folder_path):
        os.makedirs(post_folder_path)

    target_filename = 'item.md'

    target_file = open(post_folder_path + '/' + target_filename, 'w')
    target_file.write(header + post['chapo'] + post['content'])
    target_file.close()

    for image in post['images']:
        print('Copying image from: ', folder + '/images/' + os.path.basename(image))
        image_path = folder + '/images/' + os.path.basename(image)
        try:
            shutil.copy2(image_path, post_folder_path)
        except FileNotFoundError:
            print(bcolors.FAIL + 'Error: Image {0} doesn\'t seem to exist and has not been copied'.format(image) + bcolors.ENDC)
