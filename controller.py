#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import converter
import parser

def controller(args):
    """
    Loop over the data folder to start parsing and conversion of each file
    """
    folder_path = os.path.abspath(args.folder)

    # Get all posts from articles folder
    articles_folder_path = folder_path + '/articles/'

    for filename in os.listdir(articles_folder_path):
        # Check if its a XML file
        if os.path.splitext(filename)[-1] == '.xml':
            full_path = articles_folder_path + '/' + filename

            with open(full_path, 'r') as post:
                parsed_post = parser.parser(post)

            converter.toGrav(parsed_post, folder_path)
