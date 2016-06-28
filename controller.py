#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import converter

def controller(args):
    for filename in os.listdir(args.folder):
        # Check if its a XML file
        if os.path.splitext(filename)[-1] == '.xml':
            print('*'*80)
            print(filename)
            full_path = os.path.abspath(args.folder) + '/' + filename
            with open(full_path, 'r') as post:
                converter.convert(post)
