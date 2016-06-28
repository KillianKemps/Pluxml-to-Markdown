#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

import controller

# Main parser
parser = argparse.ArgumentParser(
    description='Convert PluXML files to Markdown')

parser.add_argument(
    'folder',
    help='Folder from where to import posts')

parser.set_defaults(
    func=controller.controller)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)  # call the default function
